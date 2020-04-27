from PyQt5.QtCore import QThread, pyqtSignal
from src.model.log_file import LogFile
from src.model import validator
from src.model.log_entry import LogEntry
from src.model.queue import Queue
from src.model.splunk import SplunkManager
from src.model.settings import cleansed_files
import os


class IngestWorker(QThread):
    finished = pyqtSignal()
    file_status = pyqtSignal(LogFile, float)
    entry_status = pyqtSignal(LogEntry, str)
    files_to_process: Queue
    directory_path: str

    def __init__(self, directory_path, copies_directory_path):
        self.directory_path = directory_path
        self.copies_directory_path = copies_directory_path
        self.files_to_process = Queue()
        self.splunk_manage = SplunkManager()
        self.progress_value = 0
        QThread.__init__(self)

    def run(self):
        for root, dirs, files in os.walk(self.directory_path):
            for file in files:
                if not file.startswith('.') and file not in cleansed_files:
                    self.files_to_process.enqueue(os.path.join(root, file))
                    cleansed_files.append(file)

        self.progress_value = (100 / self.files_to_process.size())
        print(self.progress_value)

        while not self.files_to_process.is_empty():
            line_num = 1
            file_path = self.files_to_process.dequeue()
            file_copy_path = validator.create_file_copy(file_path, self.copies_directory_path)
            file = os.path.basename(file_copy_path)
            file_name = file.split('.')
            log_file = LogFile(file, file_copy_path)
            print(file_name[1])
            if file_name[1] == 'csv':
                validator.cleanse_csv_file(file_copy_path)
                log_file.set_cleansing_status(True)
                if log_file.get_cleansing_status() is True:
                    validation_errors = validator.validate_csv_file(file_copy_path)
                    if validation_errors:
                        log_file.set_validation_status(False)
                        log_file.ear.set_ear(validation_errors)
                    else:
                        log_file.set_validation_status(True)

            if file_name[1] == 'log':
                validator.cleanse_log_file(file_copy_path)
                log_file.set_cleansing_status(True)
                if log_file.get_cleansing_status() is True:
                    validation_errors = validator.validate_log_file(file_copy_path)
                    if validation_errors:
                        log_file.set_validation_status(False)
                        log_file.ear.set_ear(validation_errors)
                    else:
                        log_file.set_validation_status(True)

            if log_file.get_validation_status() is True:
                self.splunk_manage.add_file(file_copy_path, 'testindex')  # add file to index
                log_file.set_ingestion_status(True)

                log_entries = self.splunk_manage.search(
                    f"search index=testindex source={file_copy_path} | table _time _raw "
                    f"source host | sort _time")  # query to get log entries

                for index in range(len(log_entries)):
                    uid = log_file.add_log_entry(line_num, log_entries[index]['source'], log_entries[index]['_time'],
                                                 log_entries[index]['_raw'])

                    self.entry_status.emit(log_file.get_log_entry(uid), uid)
                    line_num += 1

            self.progress_value += self.progress_value
            print(self.progress_value)
            self.file_status.emit(log_file, self.progress_value)

        self.finished.emit()


class ValidateWorker(QThread):
    file_updated = pyqtSignal(LogFile, float)
    entry_status = pyqtSignal(LogEntry, str)
    log_file: LogFile

    def __init__(self, log_file):
        self.files_to_process = Queue()
        self.splunk_manage = SplunkManager()
        self.log_file = log_file
        QThread.__init__(self)

    def run(self):
        line_num = 1
        file_path = self.log_file.get_file_path()
        file = os.path.basename(file_path)
        file_name = file.split('.')

        if file_name[1] == 'csv':
            validator.cleanse_csv_file(file_path)
            self.log_file.set_cleansing_status(True)
            if self.log_file.get_cleansing_status() is True:
                validation_errors = validator.validate_csv_file(file_path)
                if validation_errors:
                    self.log_file.set_validation_status(False)
                    self.log_file.ear.set_ear(validation_errors)
                else:
                    self.log_file.set_validation_status(True)
                    self.log_file.ear.set_ear(validation_errors)

        if file_name[1] == 'log':
            validator.cleanse_log_file(file_path)
            self.log_file.set_cleansing_status(True)
            if self.log_file.get_cleansing_status() is True:
                validation_errors = validator.validate_log_file(file_path)
                if validation_errors:
                    for key, value in validation_errors.items():
                        print(key, value)
                    self.log_file.set_validation_status(False)
                    self.log_file.ear.set_ear(validation_errors)
                else:
                    self.log_file.set_validation_status(True)
                    self.log_file.ear.set_ear(validation_errors)

        if self.log_file.get_validation_status() is True:
            self.splunk_manage.add_file(file_path, 'testindex')  # add file to index
            self.log_file.set_ingestion_status(True)

            log_entries = self.splunk_manage.search(
                f"search index=testindex source={file_path} | table _time _raw "
                f"source host | sort _time")  # query to get log entries

            for index in range(len(log_entries)):
                uid = self.log_file.add_log_entry(line_num, log_entries[index]['source'],
                                                  log_entries[index]['_time'],
                                                  log_entries[index]['_raw'])

                self.entry_status.emit(self.log_file.get_log_entry(uid), uid)
                line_num += 1

        self.file_updated.emit(self.log_file, 200)


class ForceIngestWorker(QThread):
    file_updated = pyqtSignal(LogFile, float)
    entry_status = pyqtSignal(LogEntry, str)
    log_file: LogFile

    def __init__(self, log_file):
        self.files_to_process = Queue()
        self.splunk_manage = SplunkManager()
        self.log_file = log_file
        QThread.__init__(self)

    def run(self):
        file_path = self.log_file.get_file_path()
        line_num = 1
        self.splunk_manage.add_file(file_path, 'testindex')  # add file to index

        log_entries = self.splunk_manage.search(
            f"search index=testindex source={file_path} | table _time _raw "
            f"source host | sort _time")  # query to get log entries

        for index in range(len(log_entries)):
            uid = self.log_file.add_log_entry(line_num, log_entries[index]['source'],
                                              log_entries[index]['_time'],
                                              log_entries[index]['_raw'])

            self.entry_status.emit(self.log_file.get_log_entry(uid), uid)
            line_num += 1

        self.log_file.set_acknowledged_status(True)
        self.log_file.set_ingestion_status(True)

        self.file_updated.emit(self.log_file, 200)

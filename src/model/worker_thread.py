"""worker_thread.py: A set of thread classes used during ingestion.
"""

__author__ = "Team Keikaku"
__version__ = "1.0"

import os
from time import sleep

from PyQt5.QtCore import QThread, pyqtSignal

from src.model import validator
from src.model.log_entry import LogEntry
from src.model.log_file import LogFile
from src.model.settings import cleansed_files
from src.model.splunk import SplunkManager
from src.util.queue import Queue


class IngestWorker(QThread):
    """ A thread routine for performing ingestion into Splunk."""

    finished = pyqtSignal()
    file_status = pyqtSignal(LogFile, float)
    entry_status = pyqtSignal(LogEntry)
    files_to_process: Queue
    directory_path: str
    splunk_manage: SplunkManager

    def __init__(self, directory_path, copies_directory_path, splunk_manage):
        self.directory_path = directory_path
        self.copies_directory_path = copies_directory_path
        self.files_to_process = Queue()
        self.splunk_manage = splunk_manage
        self.progress_value = 0
        QThread.__init__(self)

    def run(self):
        for root, dirs, files in os.walk(self.directory_path):
            for file in files:
                if not file.startswith('.') and file not in cleansed_files:
                    self.files_to_process.enqueue(os.path.join(root, file))
                    cleansed_files.append(file)
        if self.files_to_process.size() > 0:
            self.progress_value = (100 / self.files_to_process.size())
            print(self.progress_value)

        while not self.files_to_process.is_empty():
            line_num = 1
            file_path = self.files_to_process.dequeue()
            file_copy_path = validator.create_file_copy(file_path, self.copies_directory_path)
            file = os.path.basename(file_copy_path)
            file_name = file.split('.')
            log_file = LogFile(file, file_copy_path)

            if file_name[1] == 'csv':
                validator.cleanse_csv_file(file_path, file_copy_path)
                log_file.set_cleansing_status(True)
                if log_file.get_cleansing_status() is True:
                    validation_errors = validator.validate_csv_file(file_copy_path)
                    if validation_errors:
                        log_file.set_validation_status(False)
                        log_file.ear.set_ear(validation_errors)
                    else:
                        log_file.set_validation_status(True)

            if file_name[1] == 'log':
                validator.cleanse_log_file(file_path, file_copy_path)
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
                sleep(1)

                log_entries = self.splunk_manage.search(
                    f'search index=testindex source={file_copy_path} | eval time=strftime(_time, "%I:%M:%S %m/%d/%Y %p") '
                    f'| table time _raw source host | sort time')  # query to get log entries

                for index in range(len(log_entries)):
                    log_entry = LogEntry(line_num, log_entries[index]['source'],
                                         log_entries[index]['time'],
                                         log_entries[index]['_raw'])

                    self.entry_status.emit(log_entry)
                    line_num += 1
                log_file.set_ingestion_status(True)

            self.progress_value += self.progress_value
            print(self.progress_value)
            self.file_status.emit(log_file, self.progress_value)

        self.finished.emit()


class ValidateWorker(QThread):
    """ A thread routine for validating log_files."""

    file_updated = pyqtSignal(LogFile, float)
    entry_status = pyqtSignal(LogEntry)
    log_file: LogFile

    def __init__(self, log_file, copies_directory_path, splunk_manage):
        self.files_to_process = Queue()
        self.splunk_manage = splunk_manage
        self.copies_directory_path = copies_directory_path
        self.log_file = log_file
        QThread.__init__(self)

    def run(self):
        line_num = 1
        file_path = self.log_file.get_file_path()
        file_copy_path = validator.create_file_copy(file_path, self.copies_directory_path)
        file = os.path.basename(file_copy_path)
        file_name = file.split('.')

        if file_name[1] == 'csv':
            print(file_path)
            validator.cleanse_csv_file(file_path, file_copy_path)
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
            validator.cleanse_log_file(file_path, file_copy_path)
            self.log_file.set_cleansing_status(True)
            if self.log_file.get_cleansing_status() is True:
                validation_errors = validator.validate_log_file(file_path)
                if validation_errors:
                    self.log_file.set_validation_status(False)
                    self.log_file.ear.set_ear(validation_errors)
                else:
                    self.log_file.set_validation_status(True)
                    self.log_file.ear.set_ear(validation_errors)

        if self.log_file.get_validation_status() is True:
            self.splunk_manage.add_file(file_path, 'testindex')  # add file to index
            sleep(1)

            log_entries = self.splunk_manage.search(
                f'search index=testindex source={file_path} | eval time=strftime(_time, "%I:%M:%S %m/%d/%Y %p") '
                f'| table time _raw source host | sort time')  # query to get log entries

            for index in range(len(log_entries)):
                log_entry = LogEntry(line_num, log_entries[index]['source'],
                                     log_entries[index]['time'],
                                     log_entries[index]['_raw'])

                self.entry_status.emit(log_entry)
                line_num += 1
            self.log_file.set_ingestion_status(True)

        self.file_updated.emit(self.log_file, 200)


class ForceIngestWorker(QThread):
    """ A thread routine for performing forced ingestion into Splunk."""

    file_updated = pyqtSignal(LogFile, float)
    entry_status = pyqtSignal(LogEntry)
    log_file: LogFile

    def __init__(self, log_file, splunk_manage):
        self.files_to_process = Queue()
        self.splunk_manage = splunk_manage
        self.log_file = log_file
        QThread.__init__(self)

    def run(self):
        file_path = self.log_file.get_file_path()
        line_num = 1
        self.splunk_manage.add_file(file_path, 'testindex')  # add file to index
        sleep(1)

        log_entries = self.splunk_manage.search(
            f'search index=testindex source={file_path} | eval time=strftime(_time, "%I:%M:%S %m/%d/%Y %p") '
            f'| table time _raw source host | sort time')  # query to get log entries

        print(log_entries)

        for index in range(len(log_entries)):
            log_entry = LogEntry(line_num, log_entries[index]['source'], log_entries[index]['time'],
                                 log_entries[index]['_raw'])

            self.entry_status.emit(log_entry)
            print(log_entry)
            line_num += 1

        self.log_file.set_acknowledged_status(True)
        self.log_file.set_ingestion_status(True)

        self.file_updated.emit(self.log_file, 200)

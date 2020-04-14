from src.model.enforcement_action_report import EnforcementActionReport
from src.model.id_dictionary import IDDict
from src.model.log_entry import LogEntry


class LogFile:

    # TODO add comments
    file_name: str
    file_path: str
    log_entries: IDDict
    cleansing_status: bool
    validation_status: bool
    ingested_status: bool
    acknowledged_status: bool
    ear: EnforcementActionReport

    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path
        self.log_entries = IDDict()
        self.ear = EnforcementActionReport()
        self.cleansing_status = False
        self.validation_status = False
        self.acknowledged_status = False
        self.ingested_status = False

    def get_file_path(self) -> str:
        return self.file_path

    def get_file_name(self) -> str:
        return self.file_path

    def get_cleansing_status(self) -> bool:
        # TODO add cleansing logic to Validator class

        return self.cleansing_status

    def get_validation_status(self) -> bool:

        # TODO add validation logic Validator class
        return self.validation_status

    def get_acknowledged_status(self) -> bool:
        # TODO add validation logic Validator class
        return self.acknowledged_status

    def get_ingestion_status(self) -> bool:
        return self.ingested_status

    def set_cleansing_status(self, status):
        self.cleansing_status = status

    def set_validation_status(self, status):
        self.validation_status = status

    def set_ingestion_status(self, status):
        self.ingested_status = status

    def set_acknowledged_status(self, status):
        self.acknowledged_status = status

    def get_ear(self) -> dict:
        return self.ear.get_ear()

    def add_log_entry(self, line_number: str, source: str, time_stamp: str, description: str):
        return self.log_entries.add(LogEntry(line_number, source, time_stamp, description))

    def remove_log_entry(self, log_entry_id: int):
        self.log_entries.delete(log_entry_id)

    def get_log_entry(self, log_entry_id: int):
        return self.log_entries.get(log_entry_id)

    def log_entries(self) -> IDDict:
        return self.log_entries
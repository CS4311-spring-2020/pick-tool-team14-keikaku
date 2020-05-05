"""log_file.py: A collection of information representing a log file.
"""

__author__ = "Team Keikaku"
__version__ = "1.0"

from src.model.enforcement_action_report import EnforcementActionReport
from src.model.id_dictionary import IDDict
from src.model.log_entry import LogEntry


class LogFile:
    """A collection of information representing a significant event of an attack vector.

        Attributes
        ----------
        file_name: str
            The name of the log file.
        file_path: str
            The name of the path to the log_file.
        cleansing_status: bool
            Whether the log file has been cleansed or not.
        validation_status: bool
            Whether the log file has been validated or not.
        ingested_status: bool
            Whether the log file has been ingested or not.
        acknowledged_status: bool
            Whether the log file has been acknowledged or not.
        ear: EnforcementActionReport
            The Enforcement Action Report for the log file.
    """

    file_name: str
    file_path: str
    cleansing_status: bool
    validation_status: bool
    ingested_status: bool
    acknowledged_status: bool
    ear: EnforcementActionReport

    def __init__(self, file_name: str, file_path: str):
        """
        :param file_name: str
            The name of the log file.
        :param file_path: str
            The name of the path to the log_file.
        """

        self.file_name = file_name
        self.file_path = file_path
        self.ear = EnforcementActionReport()
        self.cleansing_status = False
        self.validation_status = False
        self.acknowledged_status = False
        self.ingested_status = False

    def get_file_path(self) -> str:
        return self.file_path

    def get_file_name(self) -> str:
        return self.file_name

    def get_cleansing_status(self) -> bool:
        return self.cleansing_status

    def get_validation_status(self) -> bool:
        return self.validation_status

    def get_acknowledged_status(self) -> bool:
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

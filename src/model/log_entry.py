"""log_entry.py: A collection of information representing a log entry.
"""

__author__ = "Team Keikaku"
__version__ = "1.0"


class LogEntry:
    """A collection of information representing a significant event of an attack vector.

        Attributes
        ----------
        line_number: int
            The line number in the log file this log entry refers to.
        timestamp: str
            The timestamp the log entry refers to.
        description: str
            A description of the log entry.
        source: str
            The source file of the log entry.
        vector_id: str
            A vector UID that the entry is assigned to.
    """

    line_number: int
    timestamp: str
    description: str
    source: str
    vector_id: str

    def __init__(self, line_number, source, time_stamp, description):
        self.line_number = line_number
        self.source = source
        self.time_stamp = time_stamp
        self.description = description
        self.vector_id = None

    def get_line_num(self) -> int:
        return self.line_number

    def get_timestamp(self) -> str:
        return self.time_stamp

    def get_description(self) -> str:
        return self.description

    def get_source(self) -> str:
        return self.source

    def get_vector_id(self) -> str:
        return self.vector_id

    def set_vector_id(self, vector_id: str):
        self.vector_id = vector_id

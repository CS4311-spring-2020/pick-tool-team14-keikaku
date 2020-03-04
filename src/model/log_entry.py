from src.model.id_dictionary import IDDict
from src.model.node import Node


class LogEntry:

    # TODO add comments
    line_number: int
    timestamp: str
    description: str
    source: str
    host: str

    def __init__(self, line_number, source, time_stamp, description):
        self.line_number = line_number
        self.source = source
        self.time_stamp = time_stamp
        self.description = description

    def get_line_num(self) -> int:
        return self.line_number

    def get_time_stamp(self) -> str:
        return self.time_stamp

    def get_time_stamp(self) -> str:
        return self.time_stamp

    def get_source(self) -> str:
        return self.source

    def get_host(self) -> str:
        return self.host
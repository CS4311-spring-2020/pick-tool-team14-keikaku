from src.model.id_dictionary import IDDict
from src.model.node import Node


class LogEntry:
    # TODO add comments
    line_number: int
    timestamp: str
    description: str
    source: str
    host: str
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

    def get_host(self) -> str:
        return self.host

    def get_vector_id(self) -> str:
        return self.vector_id

    def set_vector_id(self, vector_id: str):
        self.vector_id = vector_id

"""node.py: A collection of information representing an
significant event of an attack vector.
"""

__author__ = "Team Keikaku"

__version__ = "0.4"

from PyQt5.QtCore import QDateTime


class Node:
    """A collection of information representing a significant event of an attack vector.

    Attributes
    ----------
    name: str
        Name of the node.
    timestamp: QDateTime
        Timestamp node event occurred.
    description: str
        Description of the node.
    log_entry_reference: str
        Reference to the creating log entry UUID.
    log_creator: str
        Creator of the log entry node was created from.
    event_type: str
        Type of event the node represents.
    icon_type: str
        Icon the node shall use to display itself.
    source: str
        Source of the corresponding log entry.
    """

    name: str
    timestamp: QDateTime
    description: str
    log_entry_reference: str
    log_creator: str
    event_type: str
    icon_type: str
    source: str

    def __init__(self, name: str = '', timestamp: QDateTime = QDateTime(), description: str = '',
                 log_entry_reference: str = '', log_creator: str = '', event_type: str = '',
                 icon_type: str = '', source: str = ''):
        """
        :param name: str, optional (default is '')
            Name of the node.
        :param timestamp: QDateTime, optional  (default is QDateTime())
            Timestamp node event occurred.
        :param description: str, optional  (default is '')
            Description of the node.
        :param log_entry_reference: str, optional  (default is '')
            Reference to the creating log entry UUID.
        :param log_creator: str, optional  (default is '')
            Creator of the log entry node was created from.
        :param event_type: str, optional  (default is '')
            Type of event the node represents.
        :param icon_type: str, optional  (default is '')
            Icon the node shall use to display itself.
        :param source: str, optional  (default is '')
            Source of the corresponding log entry.
        """

        self.name = name
        self.timestamp = timestamp
        self.description = description
        self.log_entry_reference = log_entry_reference
        self.log_creator = log_creator
        self.event_type = event_type
        self.icon_type = icon_type
        self.source = source

    def time_string(self) -> str:
        """Returns the timestamp in a formatted string.

        :return str
            The formatted timestamp string.
        """

        return self.timestamp.toString('hh:mm MM/dd/yyyy A')

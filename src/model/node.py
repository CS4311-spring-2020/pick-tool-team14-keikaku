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
    timestamp: str
    description: str
    log_entry_reference: str
    log_creator: str
    event_type: str
    icon_type: str
    source: str
    visibility: bool

    def __init__(self, name: str = '',
                 timestamp: QDateTime = QDateTime.currentDateTimeUtc().toString('hh:mm MM/dd/yyyy A'),
                 description: str = '', log_entry_reference: str = '', log_creator: str = '', event_type: str = '',
                 icon_type: str = '', source: str = '', visibility: bool = True):
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
        :param visibility: bool, optional  (default is True)
            Visibility of the node.
        """

        self.name = name
        self.timestamp = timestamp
        self.description = description
        self.log_entry_reference = log_entry_reference
        self.log_creator = log_creator
        self.event_type = event_type
        self.icon_type = icon_type
        self.source = source
        self.visibility = visibility

    def set_name(self, name: str):
        self.name = name

    def set_timestamp(self, timestamp: QDateTime):
        self.timestamp = timestamp

    def set_description(self, description: str):
        self.description = description

    def set_log_entry_reference(self, log_entry_reference: str):
        self.log_entry_reference = log_entry_reference

    def set_log_creator(self, log_creator: str):
        self.log_creator = log_creator

    def set_event_type(self, event_type: str):
        self.event_type = event_type

    def set_icon_type(self, icon_type: str):
        self.icon_type = icon_type

    def set_source(self, source: str):
        self.source = source

    def set_visibility(self, visibility: bool):
        self.visibility = visibility

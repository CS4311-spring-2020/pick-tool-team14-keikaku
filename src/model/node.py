"""node.py: A collection of information representing an
significant event of an attack vector.
"""

__author__ = "Team Keikaku"

__version__ = "0.2"

from datetime import datetime


class Node:
    """A class representing a significant event of an attack vector.

    Attributes
    ----------
    name : str
        Name of the node.
    timestamp : datetime
        Timestamp node event occurred.
    description : str
        Description of the node.
    log_entry_reference : str
        Reference to the creating log entry UUID.
    log_creator : str
        Creator of the log entry node was created from.
    event_type : str
        Type of event the node represents.
    icon_type : str
        Icon the node shall use to display itself.
    source : str
        Source of the corresponding log entry.
    """


name: str
timestamp: datetime
description: str
log_entry_reference: str
log_creator: str
event_type: str
icon_type: str
source: str

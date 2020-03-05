"""event.py: Stores the attributes of the current
adversarial assessment.

    Attributes
    ----------
    name: str
        Name of the adversarial assessment.
    description: str
        Description of the adversarial assessment.
    start_time: str
        Start time of the adversarial assessment
    end_time: str
        End time of the adversarial assessment.
    Methods
    -------
    save():
        Saves this event instance to a file __filename.
    load() -> Settings
        Reads an event instance from a file __filename.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

from PyQt5.QtCore import QDateTime

from src.util import file_util

__filename: str = "event.pk"

name: str = ''
description: str = ''
start_time: QDateTime = QDateTime()
end_time: QDateTime = QDateTime()


def save():
    """Saves this settings instance to a file "settings"."""

    print('Saving event...')
    file_util.save_object([name, description, start_time, end_time], __filename)


def load():
    """Reads a settings instance from a file "settings"."""

    if file_util.check_file(__filename):
        print('Loading event...')
        global name, description, start_time, end_time
        name, description, start_time, end_time = file_util.read_file(__filename)

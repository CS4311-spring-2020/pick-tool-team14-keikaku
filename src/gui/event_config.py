"""event_config.py: Handles the event window.

    Classes
    ----------
    UiEventConfig(QDialog)
        The event window which handles the setting of
        project event information.
"""

__author__ = "Team Keikaku"

__version__ = "0.5"

import os

from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QDateTimeEdit
from PyQt5.uic import loadUi

from definitions import UI_PATH
from src.model import event


class UiEventConfig(QDialog):
    """The event window which handles the setting of
    project event information.

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
    """

    name: str
    description: str
    start_time: QDateTime
    end_time: QDateTime

    def __init__(self):
        """Initialize the event window and set all signals and slots
        associated with it.
        """

        super(UiEventConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'event_config.ui'), self)

        self.saveButton = self.findChild(QPushButton, 'saveButton')
        self.saveButton.clicked.connect(self.__save)

        self.name = self.findChild(QLineEdit, 'eventNameTextLine')
        self.description = self.findChild(QLineEdit, 'eventDescriptionTextLine')
        self.start_time = self.findChild(QDateTimeEdit, 'startDateTimeEdit')
        self.end_time = self.findChild(QDateTimeEdit, 'endDateTimeEdit')

        self.name.setText(event.name)
        self.description.setText(event.description)
        self.start_time.setDateTime(event.start_time)
        self.end_time.setDateTime(event.end_time)

        self.show()

    def __save(self):
        """Saves the event information and then closes the window."""

        event.name = self.name.text()
        event.description = self.description.text()
        event.start_time = self.start_time.dateTime()
        event.start_time = self.end_time.dateTime()
        event.save()
        self.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiEventConfig()
    app.exec_()

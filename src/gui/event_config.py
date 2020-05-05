"""event_config.py: Handles the event window.

    Classes
    ----------
    UiEventConfig(QDialog)
        The event window which handles the setting of
        project event information.
"""

__author__ = "Team Keikaku"
__version__ = "1.0"

import os

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QDateTimeEdit, QMessageBox
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
    start_time: QDateTimeEdit
        Start time of the adversarial assessment
    end_time: QDateTimeEdit
        End time of the adversarial assessment.
    """

    name: str
    description: str
    start_time: QDateTimeEdit
    end_time: QDateTimeEdit

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
        self.msg = QMessageBox()

        self.show()

    def __save(self):
        """Saves the event information and then closes the window."""

        if not self.name.text() or not self.description.text():
            self.msg.setText("<font color='red'>Name or Description is empty!</font>")
        elif self.start_time.dateTime().toPyDateTime() >= self.end_time.dateTime().toPyDateTime():
            self.msg.setText("<font color='red'>Invalid end time!</font>")
        else:
            self.msg.setText("<font color='green'>Event Saved!</font>")
            event.saved = True
            event.name = self.name.text()
            event.description = self.description.text()
            event.start_time = self.start_time.dateTime()
            # print(event.start_time)
            event.end_time = self.end_time.dateTime()
            # print(event.end_time)
            event.save()
            self.close()
        self.msg.exec()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiEventConfig()
    app.exec_()

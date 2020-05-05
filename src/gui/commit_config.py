"""commit_config.py: Handles the commit window.

    Classes
    ----------
    UiCommitConfig(QDialog)
        The commit window which handles the committing of log entry
        and vector changes.
"""

__author__ = "Team Keikaku"
__version__ = "0.4"

import os

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QTextEdit
from PyQt5.uic import loadUi

from definitions import UI_PATH
from src.model.id_dictionary import IDDict


class UiCommitConfig(QDialog):
    """The commit window which handles the committing of log entry
    and vector changes.

    save: pyqtSignal
        A pyQT signal emitted when the commit button is clicked.
    load: pyqtSignal
        A pyQT signal emitted when the undo button is clicked.
    """

    save: pyqtSignal = pyqtSignal()
    load: pyqtSignal = pyqtSignal()

    def __init__(self, vector_dictionary: IDDict):
        """Initialize the commit window and set all signals and slots
        associated with it.

        :param vector_dictionary: IDDict
            The vector dictionary to display changes for.
        """

        super(UiCommitConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'commit_config.ui'), self)

        self.vector_dictionary = vector_dictionary

        self.changeList = self.findChild(QTextEdit, 'changeListText')
        # TODO: display changes to the dictionary

        self.commitButton = self.findChild(QPushButton, 'commitButton')
        self.commitButton.clicked.connect(self.__commit)
        self.undoButton = self.findChild(QPushButton, 'undoButton')
        self.undoButton.clicked.connect(self.__undo)

        self.show()

    def __commit(self):
        """Commits changes to the vector dictionary."""

        self.save.emit()

    def __undo(self):
        """Undoes changes to the vector dictionary."""

        self.load.emit()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiCommitConfig()
    app.exec_()

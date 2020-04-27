"""commit_config.py: Handles the commit window.

    Classes
    ----------
    UiCommitConfig(QDialog)
        The commit window which handles the committing of log entry
        and vector changes.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

import os

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QTextEdit
from PyQt5.uic import loadUi

from definitions import UI_PATH
from src.model.id_dictionary import IDDict


class UiCommitConfig(QDialog):
    """The commit window which handles the committing of log entry
    and vector changes.
    """

    def __init__(self, vector_dictionary: IDDict):
        """Initialize the commit window and set all signals and slots
        associated with it.
        """

        super(UiCommitConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'change_config.ui'), self)

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

        self.vector_dictionary.save()

    def __undo(self):
        """Undoes changes to the vector dictionary."""

        self.vector_dictionary.load()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiCommitConfig()
    app.exec_()

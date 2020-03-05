"""directory_config.py: Handles the directory window.

    Classes
    ----------
    UiDirectoryConfig(QDialog)
        The directory window which handles the setting of
        file directory paths.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

import os

from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from PyQt5.uic import loadUi

from definitions import UI_PATH
from src.model import settings


class UiDirectoryConfig(QDialog):
    """The directory window which handles the setting of
    file directory paths.
    """

    def __init__(self):
        """Initialize the directory window and set all signals and slots
        associated with it.
        """

        super(UiDirectoryConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'directory_config.ui'), self)

        self.redTeamText = self.findChild(QLineEdit, 'redTeamText')
        self.redTeamText.insert(settings.red_team_folder)
        self.blueTeamText = self.findChild(QLineEdit, 'blueTeamText')
        self.blueTeamText.insert(settings.blue_team_folder)
        self.whiteTeamText = self.findChild(QLineEdit, 'whiteTeamText')
        self.whiteTeamText.insert(settings.white_team_folder)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiDirectoryConfig()
    app.exec_()

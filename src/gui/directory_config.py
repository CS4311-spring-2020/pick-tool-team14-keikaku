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
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.uic import loadUi

from definitions import UI_PATH
from src.model import settings


class UiDirectoryConfig(QDialog):
    """The directory window which handles the setting of
    file directory paths.
    """

    start_ingestion = pyqtSignal()

    def __init__(self):
        """Initialize the directory window and set all signals and slots
        associated with it.
        """

        super(UiDirectoryConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'directory_config.ui'), self)

        self.dialog = QFileDialog
        self.currentText = None

        self.rootText = self.findChild(QLineEdit, 'rootDirectoryText')
        self.rootText.insert(settings.root_folder)
        self.redTeamText.insert(settings.red_team_folder)
        self.blueTeamText = self.findChild(QLineEdit, 'blueTeamText')
        self.blueTeamText.insert(settings.blue_team_folder)
        self.whiteTeamText = self.findChild(QLineEdit, 'whiteTeamText')
        self.whiteTeamText.insert(settings.white_team_folder)

        self.rootDirectoryButton = self.findChild(QPushButton, 'rootDirectoryButton')
        self.rootDirectoryButton.clicked.connect(self.__file_select_root)
        self.redTeamDirectoryButton = self.findChild(QPushButton, 'redTeamDirectoryButton')
        self.redTeamDirectoryButton.clicked.connect(self.__file_select_red)
        self.blueTeamDirectoryButton = self.findChild(QPushButton, 'blueTeamDirectoryButton')
        self.blueTeamDirectoryButton.clicked.connect(self.__file_select_blue)
        self.whiteTeamDirectoryButton = self.findChild(QPushButton, 'whiteTeamDirectoryButton')
        self.whiteTeamDirectoryButton.clicked.connect(self.__file_select_white)

        self.ingest = self.findChild(QPushButton, "startDataIngestionButton")
        self.ingest.clicked.connect(self.__start_ingestion)

        self.msg = QMessageBox()

        self.show()

    def __file_select_root(self):
        dir_path = str(self.dialog.getExistingDirectory())
        self.rootText.setText(dir_path)

    def __file_select_red(self):
        dir_path = str(self.dialog.getExistingDirectory())
        self.redTeamText.setText(dir_path)

    def __file_select_blue(self):
        dir_path = str(self.dialog.getExistingDirectory())
        self.blueTeamText.setText(dir_path)

    def __file_select_white(self):
        dir_path = str(self.dialog.getExistingDirectory())
        self.whiteTeamText.setText(dir_path)

    def __start_ingestion(self):
        dir_match = []
        valid_structure = False

        for root, dirs, files in os.walk(self.rootText.text()):
            for dir in dirs:
                dir_match.append(os.path.join(root, dir))

        if len(dir_match) == 3:
            if self.redTeamText.text() not in dir_match:
                self.msg.setText("<font color='red'>Red team directory not in Root directory!</font>")
            if self.blueTeamText.text() not in dir_match:
                self.msg.setText("<font color='red'>Blue team directory not in Root directory!</font>")
            if self.whiteTeamText.text() not in dir_match:
                self.msg.setText("<font color='red'>White team directory not in Root directory!</font>")
            else:
                valid_structure = True

        else:
            self.msg.setText(f"<font color='red'>Three directories expected {len(dir_match)} found!</font>")

        if valid_structure:
            self.msg.setText("<font color='green'>Directory Structure is valid!</font>")
            settings.root_folder = self.rootText.text()
            settings.red_team_folder = self.redTeamText.text()
            settings.blue_team_folder = self.blueTeamText.text()
            settings.white_team_folder = self.whiteTeamText.text()
            settings.valid_structure = True
            self.start_ingestion.emit()

        self.msg.exec()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiDirectoryConfig()
    app.exec_()

#!/usr/bin/env python

"""main.py: Handles the main window and offers an entry-point to the
system.
"""

__author__ = "Team Keikaku"

__version__ = "0.2"

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi
from src import settings
from src.change_config import UiChangeConfig
from src.directory_config import UiDirectoryConfig
from src.event_config import UiEventConfig
from src.export_config import UiExportConfig
from src.filter_config import UiFilterConfig
from src.icon_config import UiIconConfig
from src.relationship_config import UiRelationshipConfig
from src.team_config import UiTeamConfig
from src.vector_config import UiVectorConfig
from src.vector_db_analyst import UiVectorDBAnalyst
from src.vector_db_lead import UiVectorDBLead


class Ui(QMainWindow):
    """The main window which serves as an entry point to the application
    and provides the bulk of the system's interface.
    """

    def __init__(self):
        """Initialize the main window and set all signals and slots
        associated with it.
        """

        super(Ui, self).__init__()
        loadUi('../ui/main_window.ui', self)

        self.teamButton = self.findChild(QPushButton, 'teamButton')
        self.teamButton.clicked.connect(self.__execute_team_config)
        self.eventButton = self.findChild(QPushButton, 'eventButton')
        self.eventButton.clicked.connect(self.__execute_event_config)
        self.vectorButton = self.findChild(QPushButton, 'vectorButton')
        self.vectorButton.clicked.connect(self.__execute_vector_config)
        self.filterButton = self.findChild(QPushButton, 'filterButton')
        self.filterButton.clicked.connect(self.__execute_filter_config)
        self.commitButton = self.findChild(QPushButton, 'commitButton')
        self.commitButton.clicked.connect(self.__execute_change_config)
        self.syncButton = self.findChild(QPushButton, 'syncButton')
        self.syncButton.clicked.connect(self.__execute_vector_db)
        self.exportButton = self.findChild(QPushButton, 'exportButton')
        self.exportButton.clicked.connect(self.__execute_export_config)
        self.directoryButton = self.findChild(QPushButton, 'directoryButton')
        self.directoryButton.clicked.connect(self.__execute_directory_config)
        self.iconButton = self.findChild(QPushButton, 'iconButton')
        self.iconButton.clicked.connect(self.__execute_icon_config)
        self.relationshipButton = self.findChild(QPushButton, 'relationshipsButton')
        self.relationshipButton.clicked.connect(self.__execute_relationship_config)

        self.show()

    def __execute_change_config(self):
        """Open the change configuration window."""

        self.change_window = UiChangeConfig()
        self.change_window.show()

    def __execute_directory_config(self):
        """Open the directory configuration window."""

        self.directory_window = UiDirectoryConfig()
        self.directory_window.show()

    def __execute_event_config(self):
        """Open the event configuration window."""

        self.event_window = UiEventConfig()
        self.event_window.show()

    def __execute_export_config(self):
        """Open the export configuration window."""

        self.export_window = UiExportConfig()
        self.export_window.show()

    def __execute_filter_config(self):
        """Open the filter configuration window."""

        self.filter_window = UiFilterConfig()
        self.filter_window.show()

    def __execute_icon_config(self):
        """Open the icon configuration window."""

        self.icon_window = UiIconConfig()
        self.icon_window.show()

    def __execute_relationship_config(self):
        """Open the relationship configuration window."""

        self.relationship_window = UiRelationshipConfig()
        self.relationship_window.show()

    def __execute_team_config(self):
        """Open the team configuration window."""

        self.team_window = UiTeamConfig()
        self.team_window.show()

    def __execute_vector_config(self):
        """Open the vector configuration window."""

        self.vector_window = UiVectorConfig()
        self.vector_window.show()

    def __execute_vector_db(self):
        """Open the vector db configuration window.

        If lead status in team_config is set, open the lead window;
        otherwise open the analyst window.
        """

        if settings.lead_status:
            self.vector_db_window = UiVectorDBLead()
        else:
            self.vector_db_window = UiVectorDBAnalyst()
        self.vector_db_window.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Ui()
    app.exec_()

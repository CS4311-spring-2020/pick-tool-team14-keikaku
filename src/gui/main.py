#!/usr/bin/env python

"""main.py: Handles the main window and offers an entry-point to the
system.
"""

__author__ = "Team Keikaku"

__version__ = "0.2"

import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QTableWidget, \
    QTabWidget, QCheckBox, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from definitions import UI_PATH
from src.model import settings
from src.gui.change_config import UiChangeConfig
from src.gui.directory_config import UiDirectoryConfig
from src.gui.event_config import UiEventConfig
from src.gui.export_config import UiExportConfig
from src.gui.filter_config import UiFilterConfig
from src.gui.icon_config import UiIconConfig
from src.gui.relationship_config import UiRelationshipConfig
from src.gui.team_config import UiTeamConfig
from src.gui.vector_config import UiVectorConfig
from src.gui.vector_db_analyst import UiVectorDBAnalyst
from src.gui.vector_db_lead import UiVectorDBLead


class Ui(QMainWindow):
    """The main window which serves as an entry point to the application
    and provides the bulk of the system's interface.
    """

    def __init__(self):
        """Initialize the main window and set all signals and slots
        associated with it.
        """

        super(Ui, self).__init__()
        loadUi(os.path.join(UI_PATH, 'main_window.ui'), self)

        self.teamAction = self.findChild(QAction, 'teamAction')
        self.teamAction.triggered.connect(self.__execute_team_config)
        self.eventAction = self.findChild(QAction, 'eventAction')
        self.eventAction.triggered.connect(self.__execute_event_config)
        self.exportAction = self.findChild(QAction, 'exportAction')
        self.exportAction.triggered.connect(self.__execute_export_config)

        self.vectorButton = self.findChild(QPushButton, 'vectorButton')
        self.vectorButton.clicked.connect(self.__execute_vector_config)
        self.filterButton = self.findChild(QPushButton, 'filterButton')
        self.filterButton.clicked.connect(self.__execute_filter_config)
        self.commitButton = self.findChild(QPushButton, 'commitButton')
        self.commitButton.clicked.connect(self.__execute_change_config)
        self.syncButton = self.findChild(QPushButton, 'syncButton')
        self.syncButton.clicked.connect(self.__execute_vector_db)
        self.directoryButton = self.findChild(QPushButton, 'directoryButton')
        self.directoryButton.clicked.connect(self.__execute_directory_config)
        self.relationshipButton = self.findChild(QPushButton, 'relationshipsButton')
        self.relationshipButton.clicked.connect(self.__execute_relationship_config)

        self.logFileTable = self.findChild(QTableWidget, 'logFileTable')
        self.logFileTable.setColumnWidth(0, 100)
        self.logFileTable.setColumnWidth(1, 100)
        self.logFileTable.setColumnWidth(2, 160)
        self.logFileTable.setColumnWidth(3, 160)
        self.logFileTable.setColumnWidth(4, 160)
        self.earTable = self.findChild(QTableWidget, 'earTable')
        self.earTable.setColumnWidth(0, 120)
        self.logEntryTable = self.findChild(QTableWidget, 'logEntryTable')
        self.logEntryTable.setColumnWidth(0, 120)
        self.logEntryTable.setColumnWidth(1, 180)
        self.logEntryTable.setColumnWidth(2, 160)
        self.nodeTable = self.findChild(QTableWidget, 'nodeTable')
        self.nodeTable.setColumnWidth(0, 80)
        self.nodeTable.setColumnWidth(1, 120)
        self.nodeTable.setColumnWidth(2, 160)
        self.nodeTable.setColumnWidth(3, 160)
        self.nodeTable.setColumnWidth(4, 200)
        self.nodeTable.setColumnWidth(5, 120)
        self.nodeTable.setColumnWidth(6, 120)
        self.nodeTable.setColumnWidth(7, 120)
        self.nodeTable.setColumnWidth(8, 120)
        self.nodeTable.setColumnWidth(9, 150)

        for row in range(self.nodeTable.rowCount()):
            cell_widget = QWidget()
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.Checked)
            layout = QHBoxLayout(cell_widget)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            self.nodeTable.setCellWidget(row, 9, cell_widget)

        self.tabWidget = self.findChild(QTabWidget, 'tabWidget')
        self.tabWidget.setCurrentIndex(settings.tab_index)

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

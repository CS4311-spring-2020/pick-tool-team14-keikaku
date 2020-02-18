#!/usr/bin/env python

"""main.py: Handles the main window and offers an entry-point to the
system.
"""

__author__ = "Team Keikaku"

__version__ = "0.2"

import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QTableWidget, \
    QTabWidget, QCheckBox, QWidget, QHBoxLayout, QComboBox, QLabel
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from definitions import UI_PATH
from src.model import settings, vector
from src.gui.change_config import UiChangeConfig
from src.gui.directory_config import UiDirectoryConfig
from src.gui.event_config import UiEventConfig
from src.gui.export_config import UiExportConfig
from src.gui.filter_config import UiFilterConfig
from src.gui.relationship_config import UiRelationshipConfig
from src.gui.team_config import UiTeamConfig
from src.gui.vector_config import UiVectorConfig
from src.gui.vector_db_analyst import UiVectorDBAnalyst
from src.gui.vector_db_lead import UiVectorDBLead


class Ui(QMainWindow):
    """The main window which serves as an entry point to the application
    and provides the bulk of the system's interface.

    Parameters
    ----------
    rowPosition_node : int
        The index of the last row on the node table.
    """

    rowPosition_node: int
    vector_index_dict: dict
    active_vector: str

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
        self.rowPosition_node = self.nodeTable.rowCount()

        for row in range(self.nodeTable.rowCount()):
            self.__insert_checkbox(row, 9)

        self.descriptionLabel = self.findChild(QLabel, 'descriptionLabel_2')

        self.vector_index_dict = {}
        self.active_vector = ''
        self.vectorComboBox = self.findChild(QComboBox, 'vectorComboBox')
        for v in vector.vectors.values():
            self.vectorComboBox.addItem(v.name)
        self.vectorComboBox.currentIndexChanged.connect(self.__update_vector_view)

        self.addNodeButton = self.findChild(QPushButton, 'addNodeButton')
        self.addNodeButton.setShortcut("Ctrl+Return")
        self.addNodeButton.clicked.connect(self.__add_node)
        self.deleteNodeButton = self.findChild(QPushButton, 'deleteNodeButton')
        self.deleteNodeButton.setShortcut("Ctrl+Backspace")
        self.deleteNodeButton.clicked.connect(self.__delete_node)

        self.tabWidget = self.findChild(QTabWidget, 'tabWidget')
        self.tabWidget.setCurrentIndex(settings.tab_index)
        self.tabWidget.tabBarClicked.connect(self.__update_tab)

        self.show()

    def __execute_change_config(self):
        """Open the change configuration window."""

        self.change_window = UiChangeConfig()

    def __execute_directory_config(self):
        """Open the directory configuration window."""

        self.directory_window = UiDirectoryConfig()

    def __execute_event_config(self):
        """Open the event configuration window."""

        self.event_window = UiEventConfig()

    def __execute_export_config(self):
        """Open the export configuration window."""

        self.export_window = UiExportConfig()

    def __execute_filter_config(self):
        """Open the filter configuration window."""

        self.filter_window = UiFilterConfig()

    def __execute_relationship_config(self):
        """Open the relationship configuration window."""

        self.relationship_window = UiRelationshipConfig()

    def __execute_team_config(self):
        """Open the team configuration window."""

        self.team_window = UiTeamConfig()

    def __execute_vector_config(self):
        """Open the vector configuration window."""

        self.vector_window = UiVectorConfig()

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

    def __add_node(self):
        """Adds a node to the node table and to the node dictionary."""

        self.nodeTable.blockSignals(True)
        self.nodeTable.insertRow(self.rowPosition_node)
        self.__insert_checkbox(self.rowPosition_node, 9)
        # new_uuid = uuid.uuid4().__str__()
        # TODO: add node to node dictionary
        self.rowPosition_node += 1
        self.nodeTable.blockSignals(False)

    def __delete_node(self):
        """Removes the selected node from the node table and from the node dictionary."""

        self.nodeTable.blockSignals(True)
        if self.nodeTable.selectionModel().hasSelection():
            rows = self.nodeTable.selectionModel().selectedRows()
            indexes = []
            for row in rows:
                indexes.append(row.row())
            indexes = sorted(indexes, reverse=True)
            for rowid in indexes:
                # TODO: remove node from node dictionary
                self.nodeTable.removeRow(rowid)
                self.rowPosition_node -= 1
        self.nodeTable.blockSignals(False)

    def __insert_checkbox(self, row: int, col: int):
        """"""

        cell_widget = QWidget()
        checkbox = QCheckBox()
        checkbox.setCheckState(Qt.Checked)
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(checkbox)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        self.nodeTable.setCellWidget(row, col, cell_widget)

    def __update_tab(self, index: int):
        self.vectorComboBox.blockSignals(True)
        if index == 0:
            pass
        elif index == 1:
            pass
        elif index == 2:
            if bool(vector.vectors):
                i = 0
                self.vector_index_dict.clear()
                self.vectorComboBox.clear()
                for vector_id, v in vector.vectors.items():
                    self.vectorComboBox.addItem(v.name)
                    self.vector_index_dict[i] = vector_id
                    i += 1
        elif index == -1:
            pass
        else:
            print('Invalid tab')
        self.vectorComboBox.blockSignals(False)
        print(self.vector_index_dict)
        if bool(vector.vectors):
            if self.active_vector == '':
                self.active_vector = self.vector_index_dict[0]
                self.__update_vector_view(0)
            else:
                for vector_index, vector_id in self.vector_index_dict.items():
                    if vector_id == self.active_vector:
                        self.__update_vector_view(vector_index)
                        return
                self.__update_vector_view(0)


    def __update_vector_view(self, index: int):
        self.active_vector = self.vector_index_dict[index]
        print('Active vector set: ' + str(self.active_vector))
        v = vector.vectors.get(self.vector_index_dict[index])
        self.descriptionLabel.setText(v.description)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Ui()
    app.exec_()

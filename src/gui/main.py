#!/usr/bin/env python

"""main.py: Handles the main window and offers an entry-point to the
system.
"""

__author__ = "Team Keikaku"

__version__ = "0.5"

import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QTableWidget, \
    QTabWidget, QCheckBox, QWidget, QHBoxLayout, QComboBox, QLabel, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from definitions import UI_PATH
from src.model import settings
from src.model.id_dictionary import IDDict
from src.model.vector import ActiveVector
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

    Attributes
    ----------
    rowPosition_node : int
        The index of the last row on the node table.
    active_vector : ActiveVector
        The actively displaying vector.
    vector_dictionary : IDDictionary
        Vector dictionary to interface with.
    vector_dropdown_dictionary : dict
        Dictionary of current vector indices and corresponding vector UUIDs.
    """

    rowPosition_node: int
    active_vector: ActiveVector
    vector_dictionary: IDDict
    vector_dropdown_dictionary: dict

    def __init__(self):
        """Initialize the main window and set all signals and slots
        associated with it.
        """

        super(Ui, self).__init__()
        loadUi(os.path.join(UI_PATH, 'main_window.ui'), self)

        self.active_vector = ActiveVector()
        self.vector_dictionary = IDDict()
        self.vector_dictionary.added.connect(self.__update_all_vector_info)
        self.vector_dictionary.removed.connect(self.__update_all_vector_info)
        self.vector_dictionary.edited.connect(self.__refresh_vector_info)

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

        self.descriptionLabel = self.findChild(QLabel, 'descriptionLabel_2')
        self.descriptionLabel.setText('')

        self.vector_dropdown_dictionary = {}
        self.vectorComboBox = self.findChild(QComboBox, 'vectorComboBox')
        self.vectorComboBox.currentIndexChanged.connect(self.__update_vector_display)

        self.addNodeButton = self.findChild(QPushButton, 'addNodeButton')
        self.addNodeButton.setShortcut("Ctrl+Return")
        self.addNodeButton.clicked.connect(self.__add_node)
        self.deleteNodeButton = self.findChild(QPushButton, 'deleteNodeButton')
        self.deleteNodeButton.setShortcut("Ctrl+Backspace")
        self.deleteNodeButton.clicked.connect(self.__delete_node)

        self.tabWidget = self.findChild(QTabWidget, 'tabWidget')
        self.tabWidget.setCurrentIndex(settings.tab_index)

        self.__update_all_vector_info()

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

        self.relationship_window = UiRelationshipConfig(self.active_vector.vector)

    def __execute_team_config(self):
        """Open the team configuration window."""

        self.team_window = UiTeamConfig()

    def __execute_vector_config(self):
        """Open the vector configuration window."""

        self.vector_window = UiVectorConfig(self.vector_dictionary)

    def __execute_vector_db(self):
        """Open the vector db configuration window.

        If lead status in team_config is set, open the lead window;
        otherwise open the analyst window.
        """

        if settings.lead_status:
            self.vector_db_window = UiVectorDBLead()
        else:
            self.vector_db_window = UiVectorDBAnalyst()

    def __refresh_vector_info(self):
        """Refreshes the active vector's displayed name and description."""

        self.__update_vector_dropdown()
        self.descriptionLabel.setText(self.active_vector.vector.description)

    def __update_all_vector_info(self):
        """Updates all vector related displays."""

        self.__update_vector_dropdown()
        self.__update_vector_display()

    def __update_vector_dropdown(self):
        """Updates the vector dropdown menu."""

        if not self.vector_dictionary.empty():  # If vector dictionary is not empty
            self.vectorComboBox.blockSignals(True)
            i = 0
            self.vectorComboBox.clear()
            self.vector_dropdown_dictionary = {}
            for vector_id, v in self.vector_dictionary.items():
                self.vectorComboBox.addItem(v.name)
                self.vector_dropdown_dictionary[i] = vector_id
                if vector_id == self.active_vector.vector_id:
                    self.vectorComboBox.setCurrentIndex(i)
                i += 1
            self.vectorComboBox.blockSignals(False)

    def __update_vector_display(self):
        """Updates the displayed vector information."""

        if self.vector_dictionary.empty():  # If vector dictionary is empty
            self.active_vector.set()
            self.descriptionLabel.setText('')
            self.vectorComboBox.clear()
            self.nodeTable.setRowCount(0)
            self.rowPosition_node = 0
            if hasattr(self, 'relationship_window'):
                self.relationship_window.clear()
        else:
            if not self.active_vector.vector_id == self.vector_dropdown_dictionary \
                    .get(self.vectorComboBox.currentIndex()):
                v_id = self.vector_dropdown_dictionary.get(self.vectorComboBox.currentIndex())
                self.active_vector.set(self.vector_dictionary.get(v_id), v_id)  # update active vector
                self.descriptionLabel.setText(self.active_vector.vector.description)
                self.__construct_node_table()
                if hasattr(self, 'relationship_window'):
                    self.relationship_window.construct_relationship_table(self.active_vector.vector)

    def __construct_node_table(self):
        """Constructs the node table for the active vector."""

        self.nodeTable.setRowCount(0)
        self.rowPosition_node = 0
        # print('Constructing node table for: ' + str(v.name))
        # construct node table.
        for node_id, n in self.active_vector.vector.node_items():
            self.nodeTable.insertRow(self.rowPosition_node)
            self.nodeTable.setItem(self.rowPosition_node, 0, QTableWidgetItem(node_id))
            self.nodeTable.setItem(self.rowPosition_node, 1, QTableWidgetItem(n.name))
            self.nodeTable.setItem(self.rowPosition_node, 2, QTableWidgetItem(n.time_string()))
            self.nodeTable.setItem(self.rowPosition_node, 3, QTableWidgetItem(n.description))
            self.nodeTable.setItem(self.rowPosition_node, 4, QTableWidgetItem(n.log_entry_reference))
            self.nodeTable.setItem(self.rowPosition_node, 5, QTableWidgetItem(n.log_creator))
            self.nodeTable.setItem(self.rowPosition_node, 6, QTableWidgetItem(n.event_type))
            self.nodeTable.setItem(self.rowPosition_node, 7, QTableWidgetItem(n.icon_type))
            self.nodeTable.setItem(self.rowPosition_node, 8, QTableWidgetItem(n.source))
            self.rowPosition_node += 1
        for row in range(self.nodeTable.rowCount()):
            self.__insert_checkbox(row, 9, self.nodeTable)

    def __add_node(self):
        """Adds a blank node to the node table and to the node dictionary."""

        if self.active_vector.vector:
            self.nodeTable.blockSignals(True)
            self.nodeTable.insertRow(self.rowPosition_node)
            self.__insert_checkbox(self.rowPosition_node, 9, self.nodeTable)

            # print('Adding node to: ' + str(v.name))
            uid = self.active_vector.vector.add_node()
            self.nodeTable.setItem(self.rowPosition_node, 0, QTableWidgetItem(uid))
            self.rowPosition_node += 1
            self.nodeTable.blockSignals(False)

    def __delete_node(self):
        """Removes the selected node from the node table and from the node dictionary."""

        if self.active_vector.vector:
            self.nodeTable.blockSignals(True)
            if self.nodeTable.selectionModel().hasSelection():
                rows = self.nodeTable.selectionModel().selectedRows()
                indexes = []
                for row in rows:
                    indexes.append(row.row())
                indexes = sorted(indexes, reverse=True)
                for rowid in indexes:
                    # print('Removing node from: ' + str(v.name))
                    self.active_vector.vector.delete_node(self.nodeTable.item(rowid, 0).text())
                    self.nodeTable.removeRow(rowid)
                    self.rowPosition_node -= 1
            self.nodeTable.blockSignals(False)

    @staticmethod
    def __insert_checkbox(row: int, col: int, table: QTableWidget):
        """Inserts a centered checkbox into a given table cell.

        :param row : int
            Row index.
        :param col : int
            Column index.
        :param table : QTableWidget
            Table to insert to.
        """

        cell_widget = QWidget()
        checkbox = QCheckBox()
        checkbox.setCheckState(Qt.Checked)
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(checkbox)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        table.setCellWidget(row, col, cell_widget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Ui()
    app.exec_()

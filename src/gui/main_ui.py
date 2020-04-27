#!/usr/bin/env python

"""main_ui.py: Handles the main window and offers an entry-point to the
system.
"""

__author__ = "Team Keikaku"

__version__ = "0.5"

import os

from PyQt5.Qt import QLabel, QPixmap
from PyQt5.QtCore import Qt, QObject, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QTableWidget, \
    QTabWidget, QCheckBox, QWidget, QHBoxLayout, QComboBox, QTableWidgetItem, QMessageBox, QProgressBar, QFileDialog
from PyQt5.uic import loadUi

from definitions import UI_PATH, ICON_PATH, COPIED_FILES

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

from src.model import event, settings
from src.model.log_file import LogFile
from src.model.log_entry import LogEntry
from src.model.id_dictionary import IDDict
from src.model.vector import ActiveVector
from src.model.worker_thread import IngestWorker, ValidateWorker, ForceIngestWorker


class QComboBoxVector(QComboBox):

    row: int

    def __init__(self):
        super().__init__()
        self.row = -1

class Ui(QMainWindow):
    """The main window which serves as an entry point to the application
    and provides the bulk of the system's interface.

    Attributes
    ----------
    active_vector: ActiveVector
        Actively displaying vector.
    vector_dictionary: IDDict
        Vector dictionary to interface with.
    row_position_node: int
        Index of the last row on the node table.
    """

    active_vector: ActiveVector
    vector_dictionary: IDDict
    log_file_dictionary: IDDict

    row_position_node: int
    rowPosition_log_file: int
    rowPosition_ear: int
    rowPosition_log_entry: int

    def __init__(self):
        """Initialize the main window and set all signals and slots
        associated with it.
        """
        super(Ui, self).__init__()

        self.thread = None
        self.selected_log_file_uid = None
        self.dialog = QFileDialog
        self.log_file_dictionary = IDDict()

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
        self.relationshipButton = self.findChild(QPushButton, 'relationshipsButton')
        self.relationshipButton.clicked.connect(self.__execute_relationship_config)

        self.logFileTable = self.findChild(QTableWidget, 'logFileTable')
        self.logFileTable.itemSelectionChanged.connect(self.__update_ear_table)
        self.logFileTable.setColumnHidden(0, True)
        self.rowPosition_log_file = self.logFileTable.rowCount()
        self.logFileTable.setColumnWidth(1, 100)
        self.logFileTable.setColumnWidth(2, 300)
        self.logFileTable.setColumnWidth(3, 160)
        self.logFileTable.setColumnWidth(4, 160)
        self.logFileTable.setColumnWidth(5, 160)
        self.logFileTable.setColumnWidth(6, 160)

        self.acknowledgeButton = self.findChild(QPushButton, 'acknowledgeButton')
        self.acknowledgeButton.clicked.connect(self.__force_ingest)
        self.ingestButton = self.findChild(QPushButton, 'ingestButton')
        self.ingestButton.clicked.connect(self.__start_ingestion)
        self.validateButton = self.findChild(QPushButton, 'validateButton')
        self.directoryButton = self.findChild(QPushButton, 'directoryButton')
        self.directoryButton.clicked.connect(self.__execute_directory_config)
        self.chosenSourceLabel = self.findChild(QLabel, 'chosenSourceLabel')
        self.chosenSourceLabel.setOpenExternalLinks(True)

        self.earTable = self.findChild(QTableWidget, 'earTable')
        self.rowPosition_ear = self.earTable.rowCount()
        self.earTable.setColumnHidden(0, True)
        self.earTable.setColumnWidth(0, 120)

        self.logEntryTable = self.findChild(QTableWidget, 'logEntryTable')
        self.logEntryTable.setColumnHidden(0, True)
        self.rowPosition_log_entry = self.logEntryTable.rowCount()
        self.logEntryTable.setColumnWidth(1, 80)
        self.logEntryTable.setColumnWidth(2, 200)
        self.logEntryTable.setColumnWidth(3, 200)
        self.logEntryTable.setColumnWidth(4, 400)

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

        self.nodeTable.itemChanged.connect(self.__update_node_cell)

        self.iconButton = self.findChild(QPushButton, 'selectIconButton')
        self.iconButton.clicked.connect(self.__select_icon)

        self.row_position_node = self.nodeTable.rowCount()

        self.nodeIDCheckBox = self.findChild(QCheckBox, 'nodeIDCheckBox')
        self.nodeNameCheckBox = self.findChild(QCheckBox, 'nodeNameCheckBox')
        self.nodeTimeCheckBox = self.findChild(QCheckBox, 'nodeTimeCheckBox')
        self.nodeDescCheckBox = self.findChild(QCheckBox, 'nodeDescCheckBox')
        self.logEntryCheckBox = self.findChild(QCheckBox, 'logEntryCheckBox')
        self.logCreatorCheckBox = self.findChild(QCheckBox, 'logCreatorCheckBox')
        self.eventTypeCheckBox = self.findChild(QCheckBox, 'eventTypeCheckBox')
        self.iconTypeCheckBox = self.findChild(QCheckBox, 'iconTypeCheckBox')
        self.sourceCheckBox = self.findChild(QCheckBox, 'sourceCheckBox')
        self.nodeIDCheckBox.stateChanged.connect(self.__toggle_node_id_visibility)
        self.nodeNameCheckBox.stateChanged.connect(self.__toggle_node_name_visibility)
        self.nodeTimeCheckBox.stateChanged.connect(self.__toggle_node_time_visibility)
        self.nodeDescCheckBox.stateChanged.connect(self.__toggle_node_desc_visibility)
        self.logEntryCheckBox.stateChanged.connect(self.__toggle_log_entry_visibility)
        self.logCreatorCheckBox.stateChanged.connect(self.__toggle_log_creator_visibility)
        self.eventTypeCheckBox.stateChanged.connect(self.__toggle_event_type_visibility)
        self.iconTypeCheckBox.stateChanged.connect(self.__toggle_icon_type_visibility)
        self.sourceCheckBox.stateChanged.connect(self.__toggle_source_visibility)
        self.toggleVisCheckBox = self.findChild(QCheckBox, 'toggleVisCheckBox')
        self.toggleVisCheckBox.stateChanged.connect(self.__set_node_visibility)

        self.rowPosition_node = self.nodeTable.rowCount()
        self.descriptionLabel = self.findChild(QLabel, 'descriptionLabel_2')
        self.descriptionLabel.setText('')

        self.vectorComboBox = self.findChild(QComboBox, 'vectorComboBox')
        self.vectorComboBox.currentIndexChanged.connect(self.__update_vector_display)

        self.addNodeButton = self.findChild(QPushButton, 'addNodeButton')
        self.addNodeButton.setShortcut("Ctrl+Return")
        self.addNodeButton.clicked.connect(self.__add_blank_node)
        self.deleteNodeButton = self.findChild(QPushButton, 'deleteNodeButton')
        self.deleteNodeButton.setShortcut("Ctrl+Backspace")
        self.deleteNodeButton.clicked.connect(self.__delete_node)

        self.validateButton = self.findChild(QPushButton, 'validateButton')
        self.validateButton.clicked.connect(self.__validate_file)

        self.tabWidget = self.findChild(QTabWidget, 'tabWidget')
        self.tabWidget.setCurrentIndex(settings.tab_index)

        self.__update_all_vector_info()
        self.msg = QMessageBox()

        self.progress = self.findChild(QProgressBar, 'fileProcessProgressBar')
        self.progress.setValue(0)

        self.show()

    def __start_ingestion(self):
        if not event.saved:
            self.msg.setText("<font color='red'>Event is not Saved</font>")
            self.msg.exec()
        elif not settings.valid_structure:
            self.msg.setText("<font color='red'>Directory structure is invalid!</font>")
            self.msg.exec()
        else:
            self.acknowledgeButton.setEnabled(False)
            self.ingestButton.setEnabled(False)
            self.validateButton.setEnabled(False)
            self.directoryButton.setEnabled(False)
            self.thread = IngestWorker(settings.root_folder, COPIED_FILES)
            self.thread.finished.connect(self.__on_finished)
            self.thread.file_status.connect(self.__on_file_status)
            self.thread.entry_status.connect(self.__on_entry_status)
            self.thread.start()

    def __on_finished(self):
        self.thread.quit()
        self.acknowledgeButton.setEnabled(True)
        self.ingestButton.setEnabled(True)
        self.validateButton.setEnabled(True)
        self.directoryButton.setEnabled(True)
        self.progress.setValue(0)

    def __on_file_status(self, log_file: LogFile, value: float):
        self.logFileTable.blockSignals(True)
        self.logFileTable.insertRow(self.rowPosition_log_file)
        uid = self.log_file_dictionary.add(log_file)

        self.logFileTable.setItem(self.rowPosition_log_file, 0, QTableWidgetItem(uid))
        self.logFileTable.setItem(self.rowPosition_log_file, 1, QTableWidgetItem(log_file.file_name))
        self.logFileTable.setItem(self.rowPosition_log_file, 2, QTableWidgetItem(log_file.file_path))
        self.__insert_status_icon(self.rowPosition_log_file, 3, log_file.get_cleansing_status(), self.logFileTable)
        self.__insert_status_icon(self.rowPosition_log_file, 4, log_file.get_validation_status(), self.logFileTable)
        self.__insert_status_icon(self.rowPosition_log_file, 5, log_file.get_ingestion_status(), self.logFileTable)
        self.__insert_status_icon(self.rowPosition_log_file, 6, log_file.get_acknowledged_status(), self.logFileTable)

        self.rowPosition_log_file += 1
        self.progress.setValue(value)
        self.logFileTable.blockSignals(False)

    def __on_entry_status(self, log_entry: LogEntry, uid: str):
        self.logEntryTable.blockSignals(True)
        self.logEntryTable.insertRow(self.rowPosition_log_entry)
        print(str(log_entry.get_line_num()))
        print(log_entry.get_timestamp())

        self.logEntryTable.setItem(self.rowPosition_log_entry, 0, QTableWidgetItem(uid))
        self.logEntryTable.setItem(self.rowPosition_log_entry, 1, QTableWidgetItem(str(log_entry.get_line_num())))
        self.logEntryTable.setItem(self.rowPosition_log_entry, 2, QTableWidgetItem(log_entry.get_source()))
        self.logEntryTable.setItem(self.rowPosition_log_entry, 3, QTableWidgetItem(log_entry.get_timestamp()))
        self.logEntryTable.setItem(self.rowPosition_log_entry, 4, QTableWidgetItem(log_entry.get_description()))

        self.__insert_vector_combobox(self.rowPosition_log_entry, 5, self.logEntryTable,
                                      self.vector_dictionary.items())

        self.rowPosition_log_entry += 1
        self.logEntryTable.blockSignals(False)

    def __validate_file(self):
        if self.selected_log_file_uid is not None:
            log_file = self.log_file_dictionary.get(self.selected_log_file_uid)
            print(log_file.get_file_name())
            self.thread = ValidateWorker(log_file)
            self.thread.file_updated.connect(self.__on_file_update)
            self.thread.entry_status.connect(self.__on_entry_status)
            self.thread.start()

    def __on_file_update(self, log_file: LogFile, value: float):
        self.logFileTable.blockSignals(True)
        self.log_file_dictionary.set(self.selected_log_file_uid, log_file)
        rows = self.logFileTable.selectionModel().selectedRows()
        indexes = []
        for row in rows:
            indexes.append(row.row())
            indexes = sorted(indexes, reverse=True)
        for rowid in indexes:
            self.__insert_status_icon(rowid, 3, log_file.get_cleansing_status(), self.logFileTable)
            self.__insert_status_icon(rowid, 4, log_file.get_validation_status(), self.logFileTable)
            self.__insert_status_icon(rowid, 5, log_file.get_ingestion_status(), self.logFileTable)
            self.__insert_status_icon(rowid, 6, log_file.get_acknowledged_status(), self.logFileTable)

        self.progress.setValue(value)
        self.__on_finished()
        self.__update_ear_table()
        self.logFileTable.blockSignals(False)

    def __force_ingest(self):
        if self.selected_log_file_uid is not None:
            log_file = self.log_file_dictionary.get(self.selected_log_file_uid)
            print(log_file.get_file_name())
            self.thread = ForceIngestWorker(log_file)
            self.thread.file_updated.connect(self.__on_file_update)
            self.thread.entry_status.connect(self.__on_entry_status)
            self.thread.start()

    def __execute_change_config(self):
        """Open the change configuration window."""

        self.change_window = UiChangeConfig()

    def __execute_directory_config(self):
        """Open the directory configuration window."""

        self.directory_window = UiDirectoryConfig()
        self.directory_window.start_ingestion.connect(self.__start_ingestion)

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

    def __execute_icon_config(self):
        """Open the icon configuration window."""

        self.icon_window = UiIconConfig()

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
            for vector_id, v in self.vector_dictionary.items():
                self.vectorComboBox.addItem(v.name, vector_id)
                if vector_id == self.active_vector.vector_id:
                    self.vectorComboBox.setCurrentIndex(i)
                i += 1
            self.vectorComboBox.blockSignals(False)
            for row in range(self.nodeTable.rowCount()):
                widget = self.logEntryTable.cellWidget(self.rowPosition_log_entry, 5)
                combobox = widget.findChild(QComboBox, 'combobox')
                log_entry_id_table = self.logEntryTable.item(row, 0).text()
                for log_id, log in self.log_file_dictionary.items():
                    log_entry = log.log_entries.get(log_entry_id_table)
                    if log_entry is not None:
                        combobox.blockSignals(True)
                        combobox.clear()
                        log_entry_vector_id = log_entry.get_vector_id()
                        for vector_id, v in self.vector_dictionary.items():
                            combobox.addItem(v.name, vector_id)
                            if vector_id == log_entry_vector_id:
                                combobox.setCurrentIndex(i)
                            i += 1
                        combobox.blockSignals(False)
                        break

    def __update_vector_display(self):
        """Updates the displayed vector information."""

        if self.vector_dictionary.empty():  # If vector dictionary is empty
            self.active_vector.set()
            self.descriptionLabel.setText('')
            self.vectorComboBox.clear()
            self.nodeTable.setRowCount(0)
            self.row_position_node = 0
            if hasattr(self, 'relationship_window'):
                self.relationship_window.clear()
        else:
            if not self.active_vector.vector_id == self.vectorComboBox.currentData():
                v_id = self.vectorComboBox.currentData()
                self.active_vector.set(self.vector_dictionary.get(v_id), v_id)  # update active vector
                self.descriptionLabel.setText(self.active_vector.vector.description)
                self.__block_signals(self.nodeIDCheckBox, self.nodeNameCheckBox, self.nodeTimeCheckBox,
                                     self.nodeDescCheckBox, self.logEntryCheckBox, self.logCreatorCheckBox,
                                     self.eventTypeCheckBox, self.iconTypeCheckBox, self.sourceCheckBox,
                                     block=True)
                self.nodeIDCheckBox.setChecked(self.active_vector.vector.get_node_id_visibility())
                self.nodeNameCheckBox.setChecked(self.active_vector.vector.get_node_name_visibility())
                self.nodeTimeCheckBox.setChecked(self.active_vector.vector.get_node_time_visibility())
                self.nodeDescCheckBox.setChecked(self.active_vector.vector.get_node_desc_visibility())
                self.logEntryCheckBox.setChecked(self.active_vector.vector.get_log_entry_visibility())
                self.logCreatorCheckBox.setChecked(self.active_vector.vector.get_log_creator_visibility())
                self.eventTypeCheckBox.setChecked(self.active_vector.vector.get_event_type_visibility())
                self.iconTypeCheckBox.setChecked(self.active_vector.vector.get_icon_type_visibility())
                self.sourceCheckBox.setChecked(self.active_vector.vector.get_source_visibility())
                self.__block_signals(self.nodeIDCheckBox, self.nodeNameCheckBox, self.nodeTimeCheckBox,
                                     self.nodeDescCheckBox, self.logEntryCheckBox, self.logCreatorCheckBox,
                                     self.eventTypeCheckBox, self.iconTypeCheckBox, self.sourceCheckBox,
                                     block=False)
                self.__construct_node_table()
                if hasattr(self, 'relationship_window'):
                    self.relationship_window.construct_relationship_table(self.active_vector.vector)

    def __construct_log_entry_table(self):
        """Constructs the log entry table."""

        self.logEntryTable.setRowCount(0)
        self.rowPosition_log_entry = 0

        for log_id, log in self.log_file_dictionary.items():
            for log_entry_id, log_entry in log.log_entries.items():
                self.logEntryTable.insertRow(self.rowPosition_log_entry)
                self.logEntryTable.setItem(self.rowPosition_log_entry, 0, QTableWidgetItem(log_entry_id))
                self.logEntryTable.setItem(self.rowPosition_log_entry, 1,
                                           QTableWidgetItem(str(log_entry.get_line_num())))
                self.logEntryTable.setItem(self.rowPosition_log_entry, 2,
                                           QTableWidgetItem(log_entry.get_source()))
                self.logEntryTable.setItem(self.rowPosition_log_entry, 3, QTableWidgetItem(log_entry.get_timestamp()))
                self.logEntryTable.setItem(self.rowPosition_log_entry, 4, QTableWidgetItem(log_entry.get_description()))

                self.__insert_vector_combobox(self.rowPosition_log_entry, 5, self.logEntryTable,
                                              self.vector_dictionary.items())
                widget = self.logEntryTable.cellWidget(self.rowPosition_log_entry, 5)
                combobox = widget.findChild(QComboBoxVector, 'combobox')
                combobox.row = self.rowPosition_log_entry
                combobox.setCurrentIndex(combobox.findData(log_entry.get_vector_id))
                combobox.currentIndexChanged.connect(lambda: self.__add_node(combobox.row, combobox.currentData()))
        self.rowPosition_log_entry += 1

    def __construct_log_table(self):
        pass

    def __construct_node_table(self):
        """Constructs the node table for the active vector."""

        self.nodeTable.setRowCount(0)
        self.row_position_node = 0
        # print('Constructing node table for: ' + str(v.name))
        # construct node table.
        for node_id, n in self.active_vector.vector.node_items():
            self.nodeTable.insertRow(self.row_position_node)
            self.nodeTable.setItem(self.row_position_node, 0, QTableWidgetItem(node_id))
            self.nodeTable.setItem(self.row_position_node, 1, QTableWidgetItem(n.name))
            self.nodeTable.setItem(self.row_position_node, 2, QTableWidgetItem(n.time_string()))
            self.nodeTable.setItem(self.row_position_node, 3, QTableWidgetItem(n.description))
            self.nodeTable.setItem(self.row_position_node, 4, QTableWidgetItem(n.log_entry_reference))
            self.nodeTable.setItem(self.row_position_node, 5, QTableWidgetItem(n.log_creator))
            self.nodeTable.setItem(self.row_position_node, 6, QTableWidgetItem(n.event_type))
            self.nodeTable.setItem(self.row_position_node, 7, QTableWidgetItem(n.icon_type))
            self.nodeTable.setItem(self.row_position_node, 8, QTableWidgetItem(n.source))
            self.row_position_node += 1
        for row in range(self.nodeTable.rowCount()):
            self.__insert_checkbox(row, 9, self.nodeTable)

    def __add_blank_node(self):
        """Adds a blank node to the node table and to the node dictionary."""

        if self.active_vector.vector:
            self.nodeTable.blockSignals(True)
            self.nodeTable.insertRow(self.row_position_node)
            self.__insert_checkbox(self.row_position_node, 9, self.nodeTable)
            # print('Adding node to: ' + str(v.name))
            uid = self.active_vector.vector.add_node()
            item = QTableWidgetItem(uid)
            self.nodeTable.setItem(self.row_position_node, 0, item)
            item.setFlags((Qt.ItemIsSelectable | Qt.ItemIsEnabled))
            self.row_position_node += 1
            self.nodeTable.blockSignals(False)

    def __add_node(self, row: int, vector_id: str):
        """Adds a node from row to the vector_id's node table and to the node dictionary.
        Also removes the node from any other vector.

        :param row: int
            Log Entry table row for which to construct a node from.
        :param vector_id: str
            Vector UID to add the node to.
        """
        print('Adding node from row %d to vector %s' % (row, vector_id))
        print('Node Source: %s' % self.logEntryTable.item(row, 2).text())
        print('Node Event: %s' % self.logEntryTable.item(row, 4).text())

        log_entry_id_table = self.logEntryTable.item(row, 0).text()
        for log in self.log_file_dictionary.values():
            log_entry = log.log_entries.get(log_entry_id_table)
            if log_entry is not None:
                self.nodeTable.blockSignals(True)
                # update vector
                v_id = log_entry.get_vector_id()
                if v_id is not None:
                    print(v_id)
                    self.vector_dictionary.delete(v_id)
                log_entry.set_vector_id(vector_id)
                self.nodeTable.insertRow(self.row_position_node)
                uid = self.active_vector.vector.add_node()
                self.nodeTable.setItem(self.row_position_node, 0, QTableWidgetItem(uid))
                self.nodeTable.setItem(self.row_position_node, 2, QTableWidgetItem(log_entry.get_timestamp()))
                self.nodeTable.setItem(self.row_position_node, 3, QTableWidgetItem(log_entry.get_description()))
                self.nodeTable.setItem(self.row_position_node, 8, QTableWidgetItem(log_entry.get_source()))
                self.__insert_checkbox(self.row_position_node, 9, self.nodeTable)

                self.row_position_node += 1
                self.nodeTable.blockSignals(False)
                break

    def __update_node_cell(self, item: QTableWidgetItem):
        """Updates the node information from the cell that was just edited.

        :param item: QTableWidgetItem
            The item in the table cell which contains the information to update.
        """

        node = self.active_vector.vector.node_get(self.nodeTable.item(item.row(), 0).text())
        if item.column() == 1:
            node.set_name(item.text())
        elif item.column() == 2:
            node.set_timestamp(item.text())
        elif item.column() == 3:
            node.set_description(item.text())
        elif item.column() == 4:
            node.set_log_entry_reference(item.text())
        elif item.column() == 5:
            node.set_log_creator(item.text())
        elif item.column() == 6:
            node.set_event_type(item.text())
        elif item.column() == 7:
            node.set_icon_type(item.text())
        elif item.column() == 8:
            node.set_source(item.text())
        else:
            print('Invalid column')
            return

    def __update_ear_table(self):
        self.earTable.blockSignals(True)
        rows = self.logFileTable.selectionModel().selectedRows()
        self.earTable.setRowCount(0)
        self.rowPosition_ear = 0
        indexes = []
        for row in rows:
            indexes.append(row.row())
            indexes = sorted(indexes, reverse=True)

        for rowid in indexes:
            url = bytearray(QUrl.fromLocalFile(self.logFileTable.item(rowid, 2).text()).toEncoded()).decode()
            self.chosenSourceLabel.setText(f"<a href={url}>"
                                           f"{self.logFileTable.item(rowid, 1).text()}</a>")

            self.selected_log_file_uid = self.logFileTable.item(rowid, 0).text()
            log_file = self.log_file_dictionary.get(self.selected_log_file_uid)

            if log_file.get_ear():
                for line_num, error in log_file.get_ear():
                    self.earTable.insertRow(self.rowPosition_ear)
                    self.earTable.setItem(line_num - 1, 1, QTableWidgetItem(str(line_num)))
                    self.earTable.setItem(line_num - 1, 2, QTableWidgetItem(error))
                    self.rowPosition_ear += 1
        self.earTable.blockSignals(False)

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
                    self.row_position_node -= 1
            self.nodeTable.blockSignals(False)

    def __set_node_visibility(self, state: int):
        if state == 2:
            check = True
        elif state == 0:
            check = False
        else:
            return
        for row in range(self.nodeTable.rowCount()):
            widget = self.nodeTable.cellWidget(row, 9)
            checkbox = widget.findChild(QCheckBox, 'checkbox')
            checkbox.setChecked(check)

    def __toggle_node_id_visibility(self):
        if not self.active_vector.is_empty():
            self.active_vector.vector.toggle_node_id_visibility()

    def __toggle_node_name_visibility(self):
        if not self.active_vector.is_empty():
            self.active_vector.vector.toggle_node_name_visibility()

    def __toggle_node_time_visibility(self):
        if not self.active_vector.is_empty():
            self.active_vector.vector.toggle_node_time_visibility()

    def __toggle_node_desc_visibility(self):
        if not self.active_vector.is_empty():
            self.active_vector.vector.toggle_node_desc_visibility()

    def __toggle_log_entry_visibility(self):
        if not self.active_vector.is_empty():
            self.active_vector.vector.toggle_log_entry_visibility()

    def __toggle_log_creator_visibility(self):
        if not self.active_vector.is_empty():
            self.active_vector.vector.toggle_log_creator_visibility()

    def __toggle_event_type_visibility(self):
        if not self.active_vector.is_empty():
            self.active_vector.vector.toggle_event_type_visibility()

    def __toggle_icon_type_visibility(self):
        if not self.active_vector.is_empty():
            self.active_vector.vector.toggle_icon_type_visibility()

    def __toggle_source_visibility(self):
        if not self.active_vector.is_empty():
            self.active_vector.vector.toggle_source_visibility()

    @staticmethod
    def __block_signals(*argv: QObject, block: bool):
        """Sets block of pyQT signals for a list of QObjects.

        :param argv:
            List of QObjects.
        :param block:
            True if to block, false otherwise.
        """
        for arg in argv:
            arg.blockSignals(block)


    def __insert_checkbox(self, row: int, col: int, table: QTableWidget):
        """Inserts a centered checkbox into a given table cell.

        :param row: int
            Row index.
        :param col:  int
            Column index.
        :param table: QTableWidget
            Table to insert to.
        """

        cell_widget = QWidget()
        checkbox = QCheckBox()
        checkbox.setObjectName('checkbox')
        checkbox.setCheckState(Qt.Checked)
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(checkbox)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        table.setCellWidget(row, col, cell_widget)
        checkbox.row = row
        checkbox.toggled.connect(lambda: self.__update_node_visibility(checkbox.row, checkbox))

    def __update_node_visibility(self, row: int, checkbox: QCheckBox):
        node = self.active_vector.vector.node_get(self.nodeTable.item(row, 0).text())
        if checkbox.isChecked():
            print("here")
            node.set_visibility(True)
        else:
            print("here")
            node.set_visibility(False)

    def __insert_vector_combobox(self, row: int, col: int, table: QTableWidget, vector_dictionary: IDDict):
        """Inserts a centered combobox into a given table cell.

        :param row: int
            Row index.
        :param col: int
            Column index.
        :param table: QTableWidget
            Table to insert to.
        :param vectors: list
            List of vectors.
        """

        cell_widget = QWidget()
        combobox = QComboBoxVector()
        combobox.setObjectName('combobox')
        combobox.addItem('None', 0)
        for vector_id, v in vector_dictionary:
            combobox.addItem(v.name, vector_id)

        combobox.row = row
        combobox.currentIndexChanged.connect(lambda: self.__add_node(combobox.row, combobox.currentData()))
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(combobox)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        table.setCellWidget(row, col, cell_widget)

    def __select_icon(self):
        self.nodeTable.blockSignals(True)
        if self.nodeTable.selectionModel().hasSelection():
            indexes = []
            rows = self.nodeTable.selectionModel().selectedRows()
            for row in rows:
                indexes.append(row.row())
            indexes = sorted(indexes, reverse=True)
            for rowid in indexes:
                icon_file_path = self.dialog.getOpenFileName()[0]
                if icon_file_path:
                    file = os.path.basename(icon_file_path)
                    file_name = file.split('.')
                    if file_name[1] == 'jpg' or file_name[1] == 'png':
                        self.__insert_icon(rowid, 7, icon_file_path, self.nodeTable)
                        node = self.active_vector.vector.node_get(self.nodeTable.item(rowid, 0).text())
                        node.set_icon_type(icon_file_path)

        self.nodeTable.blockSignals(False)

    @staticmethod
    def __insert_status_icon(row: int, col: int, status: bool, table: QTableWidget):
        if status is True:
            icon_path = os.path.join(ICON_PATH, 'check.png')
        else:
            icon_path = os.path.join(ICON_PATH, 'exit.png')

        icon = QPixmap(icon_path).scaledToHeight(25).scaledToWidth(25)
        cell_widget = QLabel()
        cell_widget.setAlignment(Qt.AlignCenter)
        cell_widget.setPixmap(icon)
        table.setCellWidget(row, col, cell_widget)

    @staticmethod
    def __insert_icon(row: int, col: int, icon_path: str, table: QTableWidget):

        icon = QPixmap(icon_path).scaledToHeight(25).scaledToWidth(25)
        cell_widget = QLabel()
        cell_widget.setAlignment(Qt.AlignCenter)
        cell_widget.setPixmap(icon)
        table.setCellWidget(row, col, cell_widget)



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Ui()
    app.exec_()
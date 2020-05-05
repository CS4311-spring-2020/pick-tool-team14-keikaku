#!/usr/bin/env python

"""main_ui.py: Handles the main window and offers an entry-point to the
system.
"""

__author__ = "Team Keikaku"
__version__ = "0.9"

import os

from PyQt5.Qt import QLabel, QPixmap
from PyQt5.QtCore import Qt, QObject, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QTableWidget, \
    QTabWidget, QCheckBox, QWidget, QHBoxLayout, QComboBox, QTableWidgetItem, QMessageBox, QProgressBar, QFileDialog, \
    QSplitter
from PyQt5.uic import loadUi

from definitions import UI_PATH, ICON_PATH, COPIED_FILES
from src.gui.commit_config import UiCommitConfig
from src.gui.directory_config import UiDirectoryConfig
from src.gui.event_config import UiEventConfig
from src.gui.export_config import UiExportConfig
from src.gui.filter_config import UiFilterConfig
from src.gui.graph.graph_editor import GraphEditor
from src.gui.relationship_config import UiRelationshipConfig
from src.gui.team_config import UiTeamConfig
from src.gui.vector_config import UiVectorConfig
from src.gui.vector_db_analyst import UiVectorDBAnalyst
from src.gui.vector_db_lead import UiVectorDBLead
from src.model import event, settings
from src.model.id_dictionary import IDDict
from src.model.log_entry import LogEntry
from src.model.log_file import LogFile
from src.model.node import Node
from src.model.relationship import Relationship
from src.model.splunk import SplunkManager
from src.model.vector import ActiveVector, Vector
from src.model.worker_thread import IngestWorker, ValidateWorker, ForceIngestWorker
from src.util import file_util


class Ui(QMainWindow):
    """The main window which serves as an entry point to the application
    and provides the bulk of the system's interface.

    Attributes
    ----------
    active_vector: ActiveVector
        Actively displaying vector.
    vector_dictionary: IDDict
        Vector dictionary to interface with.
    log_file_dictionary: IDDict
        Vector dictionary to interface with.
    log_entry_dictionary: IDDict
        Vector dictionary to interface with.
    log_entry_to_vector_dictionary: dict
        Log entry to vector dictionary to interface with.
    row_position_node: int
        Index of the last row on the node table.
    row_position_log_file: int
        Index of the last row on the log_file table.
    row_position_ear: int
        Index of the last row on the EAR table.
    row_position_log_entry: int
        Index of the last row on the log_entry table.
    """

    active_vector: ActiveVector
    vector_dictionary: IDDict
    log_file_dictionary: IDDict
    log_entry_dictionary: IDDict
    log_entry_to_vector_dictionary: dict

    row_position_node: int
    row_position_log_file: int
    row_position_ear: int
    row_position_log_entry: int

    def __init__(self):
        """Initialize the main window and set all signals and slots
        associated with it.
        """

        super(Ui, self).__init__()

        self.thread = None
        self.selected_log_file_uid = None
        self.dialog = QFileDialog

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
        self.commitButton.clicked.connect(self.__execute_commit_config)
        self.syncButton = self.findChild(QPushButton, 'syncButton')
        self.syncButton.clicked.connect(self.__execute_vector_db)
        self.relationshipButton = self.findChild(QPushButton, 'relationshipsButton')
        self.relationshipButton.clicked.connect(self.__execute_relationship_config)

        self.logFileTable = self.findChild(QTableWidget, 'logFileTable')
        self.logFileTable.itemSelectionChanged.connect(self.__update_ear_table)
        self.logFileTable.setColumnHidden(0, True)
        self.row_position_log_file = self.logFileTable.rowCount()
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
        self.row_position_ear = self.earTable.rowCount()
        self.earTable.setColumnHidden(0, True)
        self.earTable.setColumnWidth(0, 120)

        self.logEntryTable = self.findChild(QTableWidget, 'logEntryTable')
        self.logEntryTable.setColumnHidden(0, True)
        self.row_position_log_entry = self.logEntryTable.rowCount()
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

        self.row_position_node = self.nodeTable.rowCount()
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

        self.msg = QMessageBox()

        self.progress = self.findChild(QProgressBar, 'fileProcessProgressBar')
        self.progress.setValue(0)

        self.active_vector = ActiveVector()
        self.load_vector_dictionary()
        self.load_log_file_dictionary()
        self.vector_dictionary.added.connect(self.__update_all_vector_info)
        self.vector_dictionary.removed.connect(self.__update_all_vector_info)
        self.vector_dictionary.edited.connect(self.__refresh_vector_info)

        # Portion to display the graph
        self.splitter = self.findChild(QSplitter, "splitter")

        self.graph_editor = GraphEditor(parent=self.splitter)

        self.load_log_entry_dictionary()
        self.log_entry_to_vector_dictionary = {}
        self.splunk_manage = SplunkManager()
        self.__splunk_connect()

        self.show()

    def __splunk_connect(self):
        splunk_connection = self.splunk_manage.connect("localhost", 8089, "admin")

        if not splunk_connection:
            #self.splunk_manage.wipe_out_index("testindex")
            self.acknowledgeButton.setEnabled(True)
            self.ingestButton.setEnabled(True)
            self.validateButton.setEnabled(True)
            self.directoryButton.setEnabled(True)
            self.load_log_entry_to_vector_dictionary()
        else:
            self.acknowledgeButton.setEnabled(False)
            self.ingestButton.setEnabled(False)
            self.validateButton.setEnabled(False)
            self.directoryButton.setEnabled(False)

    def __start_ingestion(self):
        """Begins file ingestion."""

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
            self.thread = IngestWorker(settings.root_folder, COPIED_FILES, self.splunk_manage)
            self.thread.finished.connect(self.__on_finished)
            self.thread.file_status.connect(self.__on_file_status)
            self.thread.entry_status.connect(self.__on_entry_status)
            self.thread.start()

    def __on_finished(self):
        """Cleans up ingestion thread completion."""

        self.thread.quit()
        self.progress.setValue(0)
        self.acknowledgeButton.setEnabled(True)
        self.ingestButton.setEnabled(True)
        self.validateButton.setEnabled(True)
        self.directoryButton.setEnabled(True)

    def __on_file_status(self, log_file: LogFile, value: float):
        """Inserts a new log file to the log file table.

        :param log_file: logFile
            The log file to insert.
        :param value: float
            A progress percentile value.
        """

        self.logFileTable.blockSignals(True)
        self.logFileTable.insertRow(self.row_position_log_file)
        uid = self.log_file_dictionary.add(log_file)

        self.logFileTable.setItem(self.row_position_log_file, 0, QTableWidgetItem(uid))
        self.logFileTable.setItem(self.row_position_log_file, 1, QTableWidgetItem(log_file.file_name))
        self.logFileTable.setItem(self.row_position_log_file, 2, QTableWidgetItem(log_file.file_path))
        self.__insert_status_icon(self.row_position_log_file, 3, log_file.get_cleansing_status(), self.logFileTable)
        self.__insert_status_icon(self.row_position_log_file, 4, log_file.get_validation_status(), self.logFileTable)
        self.__insert_status_icon(self.row_position_log_file, 5, log_file.get_ingestion_status(), self.logFileTable)
        self.__insert_status_icon(self.row_position_log_file, 6, log_file.get_acknowledged_status(), self.logFileTable)

        self.row_position_log_file += 1
        self.progress.setValue(value)
        self.logFileTable.blockSignals(False)

    def __on_entry_status(self, log_entry: LogEntry):
        """Inserts a new log entry to the log entry table.

        :param log_entry:
            The log entry to insert.
        """

        self.logEntryTable.blockSignals(True)
        self.logEntryTable.insertRow(self.row_position_log_entry)
        print(str(log_entry.get_line_num()))
        print(log_entry.get_timestamp())

        uid = self.log_entry_dictionary.add(log_entry)

        self.logEntryTable.setItem(self.row_position_log_entry, 0, QTableWidgetItem(uid))
        self.logEntryTable.setItem(self.row_position_log_entry, 1, QTableWidgetItem(str(log_entry.get_line_num())))
        self.logEntryTable.setItem(self.row_position_log_entry, 2, QTableWidgetItem(log_entry.get_source()))
        self.logEntryTable.setItem(self.row_position_log_entry, 3, QTableWidgetItem(log_entry.get_timestamp()))
        self.logEntryTable.setItem(self.row_position_log_entry, 4, QTableWidgetItem(log_entry.get_description()))

        self.log_entry_to_vector_dictionary[log_entry.get_description()] = {'line_num': log_entry.get_line_num(),
                                                                            'entry_id': uid, 'vector_id': '0'}

        self.__insert_vector_combobox(self.row_position_log_entry, 5, self.logEntryTable, self.vector_dictionary)

        self.row_position_log_entry += 1
        self.logEntryTable.blockSignals(False)

    def __validate_file(self):
        """Begins file validation."""

        if self.selected_log_file_uid is not None:
            log_file = self.log_file_dictionary.get(self.selected_log_file_uid)
            print(log_file.get_file_name())
            self.thread = ValidateWorker(log_file, self.splunk_manage)
            self.thread.file_updated.connect(self.__on_file_update)
            self.thread.entry_status.connect(self.__on_entry_status)
            self.thread.start()

    def __on_file_update(self, log_file: LogFile, value: float):
        """Updates the statuses of a log file.

        :param log_file:
            The log file to update statuses for.
        :param value:
            A progress percentile value.
        """

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
        """Begins forced file ingestion."""

        if self.selected_log_file_uid is not None:
            log_file = self.log_file_dictionary.get(self.selected_log_file_uid)
            print(log_file.get_file_name())
            self.thread = ForceIngestWorker(log_file, self.splunk_manage)
            self.thread.file_updated.connect(self.__on_file_update)
            self.thread.entry_status.connect(self.__on_entry_status)
            self.thread.start()

    def __execute_commit_config(self):
        """Open the change configuration window."""

        self.change_window = UiCommitConfig(self.vector_dictionary)
        self.change_window.save.connect(self.save_vector_dictionary)
        self.change_window.load.connect(self.load_vector_dictionary)
        self.change_window.save.connect(self.save_log_file_dictionary)
        self.change_window.save.connect(self.save_log_entry_to_vector_dictionary)
        self.change_window.save.connect(self.save_log_entry_dictionary)

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

        self.relationship_window = UiRelationshipConfig(self.active_vector.vector, self.nodeTable)

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

    def __update_all_vector_info(self, hard: bool = False):
        """Updates all vector related displays.

        :param: hard: bool, optional (default is False)
            Whether to perform a hard (force) update to the tables.
        """

        self.__update_vector_dropdown()
        self.__update_vector_display(hard)

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
            if self.logEntryTable.rowCount() > 0:
                for row in range(self.logEntryTable.rowCount()):
                    widget = self.logEntryTable.cellWidget(row, 5)
                    combobox = widget.findChild(QComboBox, 'combobox')
                    log_entry_id_table = self.logEntryTable.item(row, 0).text()
                    log_entry = self.log_entry_dictionary.get(log_entry_id_table)
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

    def __update_vector_display(self, hard: bool = False):
        """Updates the displayed vector information.

        :param: hard: bool, optional (default is False)
            Whether to perform a hard (force) update to the tables.
        """

        if self.vector_dictionary.empty():  # If vector dictionary is empty
            self.active_vector.set()
            self.descriptionLabel.setText('')
            self.vectorComboBox.clear()
            self.nodeTable.setRowCount(0)
            self.row_position_node = 0
            if hasattr(self, 'relationship_window'):
                self.relationship_window.clear()
        elif not self.active_vector.vector_id == self.vectorComboBox.currentData():
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
        elif hard:
            self.__construct_node_table()
            if hasattr(self, 'relationship_window'):
                self.relationship_window.construct_relationship_table(self.active_vector.vector)

        # @TODO Test this to make sure it works
        if self.active_vector.vector:
            self.graph_editor.add_vector(self.active_vector.vector)


    def __construct_log_entry_table(self):
        """Constructs the log entry table."""

        self.logEntryTable.blockSignals(True)
        self.logEntryTable.setRowCount(0)
        self.row_position_log_entry = 0

        for log_entry_id, log_entry in self.log_entry_dictionary.items():
            self.logEntryTable.insertRow(self.row_position_log_entry)
            item = QTableWidgetItem(log_entry_id)
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)
            self.logEntryTable.setItem(self.row_position_log_entry, 0, item)
            self.logEntryTable.setItem(self.row_position_log_entry, 1,
                                   QTableWidgetItem(str(log_entry.get_line_num())))
            self.logEntryTable.setItem(self.row_position_log_entry, 2,
                                   QTableWidgetItem(log_entry.get_source()))
            self.logEntryTable.setItem(self.row_position_log_entry, 3, QTableWidgetItem(log_entry.get_timestamp()))
            self.logEntryTable.setItem(self.row_position_log_entry, 4, QTableWidgetItem(log_entry.get_description()))

            self.__insert_vector_combobox(self.row_position_log_entry, 5, self.logEntryTable,
                                      self.vector_dictionary)

            self.row_position_log_entry += 1

        self.logEntryTable.blockSignals(False)

    def __construct_log_table(self):
        """Constructs the log table for the active vector."""

        self.logFileTable.blockSignals(True)

        self.logFileTable.setRowCount(0)
        self.row_position_log_file = 0

        for log_file_id, l in self.log_file_dictionary.items():
            print(l.file_name)
            self.logFileTable.insertRow(self.row_position_log_file)
            self.logFileTable.setItem(self.row_position_log_file, 0, QTableWidgetItem(log_file_id))
            self.logFileTable.setItem(self.row_position_log_file, 1, QTableWidgetItem(l.file_name))
            self.logFileTable.setItem(self.row_position_log_file, 2, QTableWidgetItem(l.file_path))
            self.__insert_status_icon(self.row_position_log_file, 3, l.get_cleansing_status(), self.logFileTable)
            self.__insert_status_icon(self.row_position_log_file, 4, l.get_validation_status(), self.logFileTable)
            self.__insert_status_icon(self.row_position_log_file, 5, l.get_ingestion_status(), self.logFileTable)
            self.__insert_status_icon(self.row_position_log_file, 6, l.get_acknowledged_status(), self.logFileTable)
            self.row_position_log_file += 1

        self.logFileTable.blockSignals(False)

    def __construct_node_table(self):
        """Constructs the node table for the active vector."""

        self.nodeTable.blockSignals(True)

        self.nodeTable.setRowCount(0)
        self.row_position_node = 0
        # print('Constructing node table for: ' + str(v.name))
        # construct node table.
        for node_id, n in self.active_vector.vector.node_items():
            self.nodeTable.insertRow(self.row_position_node)
            item = QTableWidgetItem(node_id)
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)
            self.nodeTable.setItem(self.row_position_node, 0, item)
            self.nodeTable.setItem(self.row_position_node, 1, QTableWidgetItem(n.name))
            self.nodeTable.setItem(self.row_position_node, 2, QTableWidgetItem(n.timestamp))
            self.nodeTable.setItem(self.row_position_node, 3, QTableWidgetItem(n.description))
            self.nodeTable.setItem(self.row_position_node, 4, QTableWidgetItem(n.log_entry_reference))
            self.nodeTable.setItem(self.row_position_node, 5, QTableWidgetItem(n.log_creator))
            self.nodeTable.setItem(self.row_position_node, 6, QTableWidgetItem(n.event_type))
            self.nodeTable.setItem(self.row_position_node, 7, QTableWidgetItem(n.icon_type))
            self.nodeTable.setItem(self.row_position_node, 8, QTableWidgetItem(n.source))
            self.row_position_node += 1
        for row in range(self.nodeTable.rowCount()):
            self.__insert_checkbox(row, 9, self.nodeTable)

        self.nodeTable.blockSignals(False)

    def __add_blank_node(self):
        """Adds a blank node to the node table and to the node dictionary."""

        if self.active_vector.vector:
            self.nodeTable.blockSignals(True)
            self.nodeTable.insertRow(self.row_position_node)
            self.__insert_checkbox(self.row_position_node, 9, self.nodeTable)
            # print('Adding node to: ' + str(v.name))
            uid = self.active_vector.vector.add_node()
            self.nodeTable.setItem(self.row_position_node, 2, QTableWidgetItem(
                self.active_vector.vector.node_get(uid).timestamp))
            item = QTableWidgetItem(uid)
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)
            self.nodeTable.setItem(self.row_position_node, 0, item)
            self.row_position_node += 1
            self.nodeTable.blockSignals(False)

            # @TODO For adding nodes
            if self.active_vector.vector.node_get(uid):
                self.graph_editor.add_node(self.active_vector.vector.node_get(uid))

    def __add_node(self, row: int, vector_id: str):
        """Adds a node from row to the vector_id's node table and to the node dictionary.
        Also removes the node from any other vector.

        :param row: int
            Log Entry table row for which to construct a node from.
        :param vector_id: str
            Vector UID to add the node to.
        """

        # print('Adding node from row %d to vector %s' % (row, vector_id))
        # print('Node Source: %s' % self.logEntryTable.item(row, 2).text())
        # print('Node Event: %s' % self.logEntryTable.item(row, 4).text())

        log_entry_id_table = self.logEntryTable.item(row, 0).text()
        log_entry = self.log_entry_dictionary.get(log_entry_id_table)

        if log_entry is not None:
            self.nodeTable.blockSignals(True)
            self.vector_dictionary.blockSignals(True)
            # remove node from old vector
            v_id = log_entry.get_vector_id()
            if v_id != '0':  # remove node from old vector
                self.vector_dictionary.get(v_id).delete_node(log_entry.get_node_id())
                if v_id == self.active_vector.vector_id:  # if vector is active
                    for row in range(self.row_position_node):
                        if self.nodeTable.item(row, 4).text() == log_entry_id_table:
                            self.nodeTable.removeRow(row)
                            self.row_position_node -= 1
                            break
            log_entry.set_node_id(None)
            log_entry.set_vector_id(vector_id)
            if vector_id is not None:  # add node to new vector
                uid = self.active_vector.vector.add_node()
                log_entry.set_node_id(uid)
                node = self.active_vector.vector.node_get(uid)
                # TODO: add values to the node object

                self.nodeTable.insertRow(self.row_position_node)
                item = QTableWidgetItem(uid)
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.nodeTable.setItem(self.row_position_node, 0, item)
                self.nodeTable.setItem(self.row_position_node, 2, QTableWidgetItem(log_entry.get_timestamp()))
                self.nodeTable.setItem(self.row_position_node, 3, QTableWidgetItem(log_entry.get_description()))
                self.nodeTable.setItem(self.row_position_node, 8, QTableWidgetItem(log_entry.get_source()))
                self.__insert_checkbox(self.row_position_node, 9, self.nodeTable)

                self.row_position_node += 1
                # @TODO For adding created node
                if self.active_vector.vector.node_get(uid):
                    self.graph_editor.add_node(self.active_vector.vector.node_get(uid))
            self.nodeTable.blockSignals(False)
            self.vector_dictionary.blockSignals(False)




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
            print('Invalid column %d' % item.column())
            return

    def __update_ear_table(self):
        """Updates the Enforcement Action Report table."""

        self.earTable.blockSignals(True)
        rows = self.logFileTable.selectionModel().selectedRows()
        self.earTable.setRowCount(0)
        self.row_position_ear = 0
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
                for line_num, error in log_file.get_ear().items():
                    self.earTable.insertRow(self.row_position_ear)
                    self.earTable.setItem(line_num - 1, 1, QTableWidgetItem(str(line_num)))
                    self.earTable.setItem(line_num - 1, 2, QTableWidgetItem(error))
                    self.row_position_ear += 1
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
        """Sets the node visibility."""

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

        :param argv: QObject
            List of QObjects.
        :param block: bool
            True if to block, false otherwise.
        """
        for arg in argv:
            arg.blockSignals(block)

    def __insert_checkbox(self, row: int, col: int, table: QTableWidget):
        """Inserts a centered checkbox into a given table cell.

        :param row: int
            Row index.
        :param col: int
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
        """Updates the node visibility.

        :param row: int
            The row on the node table.
        :param checkbox:
            The node visibility checkbox.
        :return: bool
            True if the checkbox is checked, false otherwise.
        """

        node = self.active_vector.vector.node_get(self.nodeTable.item(row, 0).text())
        if checkbox.isChecked():
            node.set_visibility(True)
        else:
            node.set_visibility(False)

    def __insert_vector_combobox(self, row: int, col: int, table: QTableWidget, vector_dictionary: IDDict):
        """Inserts a centered combobox into a given table cell.

        :param row: int
            Row index.
        :param col: int
            Column index.
        :param table: QTableWidget
            Table to insert to.
        :param vector_dictionary: IDDict
            List of vectors and associated UIDs.
        """

        cell_widget = QWidget()
        combobox = QComboBox()
        combobox.setObjectName('combobox')
        combobox.addItem('None', '0')
        for vector_id, v in vector_dictionary.items():
            combobox.addItem(v.name, vector_id)

        combobox.currentIndexChanged.connect(lambda r=row: self.__add_node(r, combobox.currentData()))
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(combobox)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        table.setCellWidget(row, col, cell_widget)

    def __select_icon(self):
        """Assigns the selected icon to a node."""

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
        """Inserts a status icon to a table cell.

        :param row: int
            Row index.
        :param col: int
            Column index.
        :param status: bool
            The status to determine which icon to be inserted.
        :param table: QTableWidget
            The table to insert the status icon into.
        """

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
        """Inserts an icon into a table cell.

        :param row: int
            Row index.
        :param col: int
            Column index.
        :param icon_path: str
            The file path to the icon to be inserted.
        :param table: QTableWidget
            The table to insert the icon into.
        """

        icon = QPixmap(icon_path).scaledToHeight(25).scaledToWidth(25)
        cell_widget = QLabel()
        cell_widget.setAlignment(Qt.AlignCenter)
        cell_widget.setPixmap(icon)
        table.setCellWidget(row, col, cell_widget)

    def save_vector_dictionary(self):
        """Saves the vector dictionary to a file."""

        # print('Saving dict...')
        v_dict = {'active': self.active_vector.vector_id}
        for v_id, v in self.vector_dictionary.items():
            vector = {
                'name': v.name,
                'description': v.description,
                'property_visibility': v.property_visibility
            }
            n_dict = {}
            for n_id, n in v.node_items():
                n_dict[n_id] = [n.name, n.timestamp, n.description, n.log_entry_reference, n.log_creator,
                                n.event_type, n.icon_type, n.source, n.visibility]
            r_dict = {}
            for r_id, r in v.relationship_items():
                r_dict[r_id] = [r.parent, r.child, r.label]
            vector['nodes'] = n_dict
            vector['relationships'] = r_dict
            v_dict[v_id] = vector

        file_util.save_object(v_dict, 'vector_dictionary.pk')

    def load_vector_dictionary(self):
        """Reads a vector dictionary from a file."""

        if file_util.check_file('vector_dictionary.pk'):
            # print('Loading dict...')
            v_dict = {}
            data = file_util.read_file('vector_dictionary.pk')
            active_vector_id = data.pop('active')
            for v_id, v in data.items():
                n_dict = {}
                for n_id, n in v['nodes'].items():
                    n_dict[n_id] = Node(name=n[0], timestamp=n[1], description=n[2], log_entry_reference=n[3],
                                        log_creator=n[4], event_type=n[5], icon_type=n[6], source=n[7], visibility=n[8])
                r_dict = {}
                for r_id, r in v['relationships'].items():
                    r_dict[r_id] = Relationship(parent=r[0], child=n[1], label=n[2])
                vector = Vector(vector_name=v['name'], vector_desc=v['description'],
                                property_visibility=v['property_visibility'], nodes=n_dict, relationships=r_dict)
                v_dict[v_id] = vector
            self.vector_dictionary = IDDict(v_dict)
            self.active_vector.set(self.vector_dictionary.get(active_vector_id), active_vector_id)
        else:
            self.vector_dictionary = IDDict()
        self.__update_all_vector_info(True)

    def save_log_file_dictionary(self):
        """Saves the log file dictionary to a file."""

        # print('Saving dict...')
        l_dict = {}
        for l_id, l in self.log_file_dictionary.items():
            log_file = {'file_name': l.file_name, 'file_path': l.file_path, 'cleansing_status': l.cleansing_status,
                        'validation_status': l.validation_status, 'acknowledged_status': l.acknowledged_status,
                        'ingested_status': l.ingested_status, 'ear': l.get_ear()}
            l_dict[l_id] = log_file

        file_util.save_object(l_dict, 'log_file_dictionary.pk')

    def load_log_file_dictionary(self):
        """Reads a log file dictionary from a file."""

        if file_util.check_file('log_file_dictionary.pk'):
            # print('Loading dict...')
            l_dict = {}
            data = file_util.read_file('log_file_dictionary.pk')
            for l_id, l in data.items():

                log_file = LogFile(l['file_name'], l['file_path'])
                log_file.set_cleansing_status(l['cleansing_status'])
                log_file.set_validation_status(l['validation_status'])
                log_file.set_acknowledged_status(l['acknowledged_status'])
                log_file.set_ingestion_status(l['ingested_status'])
                log_file.ear.set_ear(l['ear'])

                l_dict[l_id] = log_file

            self.log_file_dictionary = IDDict(l_dict)

        else:
            self.log_file_dictionary = IDDict()
        self.__construct_log_table()

    def save_log_entry_to_vector_dictionary(self):
        """Saves the log entry to vector id dictionary to a file."""

        print('Saving dict...')

        file_util.save_object(self.log_entry_to_vector_dictionary, 'log_entry_to_vector_dictionary.pk')

    def load_log_entry_to_vector_dictionary(self):
        """Reads a log entry to vector id dictionary from a file."""

        if file_util.check_file('log_entry_to_vector_dictionary.pk'):
            print('Loading dict...')
            data = file_util.read_file('log_entry_to_vector_dictionary.pk')
            print(data)

            for ev_id, entry_dict in data.items():
                print(data[ev_id]["line_num"])
                print(data[ev_id]["entry_id"])
                print(data[ev_id]["vector_id"])

            self.log_entry_to_vector_dictionary = data

        else:
            self.log_file_dictionary = IDDict()
        self.__construct_log_table()

    def save_log_entry_dictionary(self):
        """Saves the log entry dictionary to a file."""

        # print('Saving dict...')
        le_dict = {}
        for le_id, le in self.log_entry_dictionary.items():
            log_entry = {'line_number': le.line_number, 'timestamp': le.time_stamp, 'description': le.description,
                        'source': le.source, 'vector_id': le.vector_id}
            le_dict[le_id] = log_entry

        file_util.save_object(le_dict, 'log_entry_dictionary.pk')

    def load_log_entry_dictionary(self):
        """loads the log entry dictionary to a file."""
        if file_util.check_file('log_entry_dictionary.pk'):
            # print('Loading dict...')
            le_dict = {}
            data = file_util.read_file('log_entry_dictionary.pk')
            for le_id, le in data.items():
                log_entry = LogEntry(le['line_number'], le['timestamp'], le['description'], le['source'])

                log_entry.set_vector_id(le['vector_id'])

                le_dict[le_id] = log_entry

            self.log_entry_dictionary = IDDict(le_dict)

        else:
            self.log_entry_dictionary = IDDict()
        self.__construct_log_entry_table()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Ui()
    app.exec_()

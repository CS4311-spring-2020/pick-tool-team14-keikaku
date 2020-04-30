"""vector_config.py: Handles the vector window.

    Classes
    ----------
    UiVectorConfig(QFrame)
        The vector window which handles the adding, editing, and deleting
        of vectors and their descriptions.
"""

__author__ = "Team Keikaku"

__version__ = "2.0"

import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFrame, QTableWidget, QPushButton, QTableWidgetItem
from PyQt5.uic import loadUi

from definitions import UI_PATH
from src.model.id_dictionary import IDDict
from src.model.vector import Vector


class UiVectorConfig(QFrame):
    """The vector window which handles the adding, editing, and deleting
    of vectors and their descriptions.

    Parameters
    ----------
    row_position: int
        The index of the last row on the vector table.
    vector_dictionary: VectorDictionary
        Vector dictionary to interface with.
    """

    row_position: int
    vector_dictionary: IDDict

    def __init__(self, vector_dictionary: IDDict):
        """Initialize the vector window and set all signals and slots
        associated with it.

        :param vector_dictionary: IDDict
            Vector dictionary to interface with.
        """

        super(UiVectorConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'vector_config.ui'), self)

        self.vectorTable = self.findChild(QTableWidget, 'vectorTable')
        # self.iconTable.setColumnHidden(0, True)
        self.vectorTable.setColumnWidth(1, 120)
        self.vectorTable.itemChanged.connect(self.__update_cell)

        self.addButton = self.findChild(QPushButton, 'addVectorButton')
        self.addButton.clicked.connect(self.__add_vector)
        self.deleteButton = self.findChild(QPushButton, 'deleteVectorButton')
        self.deleteButton.clicked.connect(self.__delete_vector)

        if vector_dictionary:
            self.construct_vector_table(vector_dictionary)

        self.show()

    def construct_vector_table(self, vector_dictionary: IDDict):
        """Constructs the vector table.

        :param vector_dictionary: Vector
            The vector_dictionary to display.
        """
        self.vectorTable.blockSignals(True)
        self.vector_dictionary = vector_dictionary
        self.vectorTable.setRowCount(0)
        self.row_position = 0
        # print('Constructing vector table')
        for vector_id, v in vector_dictionary.items():
            self.vectorTable.insertRow(self.row_position)
            item = QTableWidgetItem(vector_id)
            item.setFlags(item.flags() ^ (Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            self.vectorTable.setItem(self.row_position, 0, item)
            self.vectorTable.setItem(self.row_position, 1, QTableWidgetItem(v.name))
            self.vectorTable.setItem(self.row_position, 2, QTableWidgetItem(v.description))
            self.row_position += 1
        self.vectorTable.blockSignals(False)

    def __add_vector(self):
        """Adds a vector to the vector table and to the vector dictionary."""

        self.vectorTable.blockSignals(True)
        self.vectorTable.insertRow(self.row_position)
        uid = self.vector_dictionary.add(Vector('New Vector'))
        item = QTableWidgetItem(uid)
        item.setFlags(item.flags() ^ (Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
        self.vectorTable.setItem(self.row_position, 0, item)
        self.vectorTable.setItem(self.row_position, 1, QTableWidgetItem('New Vector'))
        self.row_position += 1
        self.vectorTable.blockSignals(False)

    def __delete_vector(self):
        """Removes the selected vector from the vector table and from the vector dictionary."""

        self.vectorTable.blockSignals(True)
        if self.vectorTable.selectionModel().hasSelection():
            rows = self.vectorTable.selectionModel().selectedRows()
            indexes = []
            for row in rows:
                indexes.append(row.row())
            indexes = sorted(indexes, reverse=True)
            for rowid in indexes:
                self.vector_dictionary.delete(self.vectorTable.item(rowid, 0).text())
                self.vectorTable.removeRow(rowid)
                self.row_position -= 1
        self.vectorTable.blockSignals(False)

    def __update_cell(self, item: QTableWidgetItem):
        """Updates the vector information from the cell that was just edited.

        :param item: QTableWidgetItem
            The item in the table cell which contains the information to update.
        """

        v = self.vector_dictionary.get(self.vectorTable.item(item.row(), 0).text())
        if item.column() == 1:
            v.edit_name(item.text())
        elif item.column() == 2:
            v.edit_desc(item.text())
        else:
            print('Invalid column')
            return
        self.vector_dictionary.edit()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiVectorConfig()
    app.exec_()

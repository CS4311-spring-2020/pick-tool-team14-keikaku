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
import uuid

from PyQt5.QtWidgets import QApplication, QFrame, QTableWidget, QPushButton, QTableWidgetItem
from PyQt5.uic import loadUi
from definitions import UI_PATH
from src.model.vector import VectorDictionary


class UiVectorConfig(QFrame):
    """The vector window which handles the adding, editing, and deleting
    of vectors and their descriptions.

    Parameters
    ----------
    rowPosition : int
        The index of the last row on the vector table.
    vector_dictionary : VectorDictionary
        Vector dictionary to interface with.
    """

    rowPosition: int
    vector_dictionary: VectorDictionary

    def __init__(self, vector_dictionary: VectorDictionary):
        """Initialize the vector window and set all signals and slots
        associated with it.

        :param
            Vector dictionary to interface with.
        """

        super(UiVectorConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'vector_config.ui'), self)

        self.vector_dictionary = vector_dictionary

        self.vectorTable = self.findChild(QTableWidget, 'vectorTable')
        # self.iconTable.setColumnHidden(0, True)
        self.vectorTable.setColumnWidth(1, 120)
        self.rowPosition = self.vectorTable.rowCount()

        self.addButton = self.findChild(QPushButton, 'addVectorButton')
        self.addButton.clicked.connect(self.__add_vector)
        self.deleteButton = self.findChild(QPushButton, 'deleteVectorButton')
        self.deleteButton.clicked.connect(self.__delete_vector)

        # construct vector table.
        for vector_id, v in self.vector_dictionary.items():
            self.vectorTable.insertRow(self.rowPosition)
            self.vectorTable.setItem(self.rowPosition, 0, QTableWidgetItem(vector_id))
            self.vectorTable.setItem(self.rowPosition, 1, QTableWidgetItem(v.name))
            self.vectorTable.setItem(self.rowPosition, 2, QTableWidgetItem(v.description))
            self.rowPosition += 1

        self.vectorTable.itemChanged.connect(self.__update_cell)

        self.show()

    def __add_vector(self):
        """Adds a vector to the vector table and to the vector dictionary."""

        self.vectorTable.blockSignals(True)
        self.vectorTable.insertRow(self.rowPosition)
        new_uuid = uuid.uuid4().__str__()
        self.vector_dictionary.add_vector(new_uuid, 'New Vector')
        self.vectorTable.setItem(self.rowPosition, 0, QTableWidgetItem(new_uuid))
        self.vectorTable.setItem(self.rowPosition, 1, QTableWidgetItem('New Vector'))
        self.rowPosition += 1
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
                self.vector_dictionary.delete_vector(self.vectorTable.item(rowid, 0).text())
                self.vectorTable.removeRow(rowid)
                self.rowPosition -= 1
        self.vectorTable.blockSignals(False)

    def __update_cell(self, item: QTableWidgetItem):
        """Updates the vector information from the cell that was just edited.

        Parameters
        ----------
        item : QTableWidgetItem
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
        self.vector_dictionary.edit_vector()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiVectorConfig()
    app.exec_()

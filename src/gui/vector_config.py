"""vector_config.py: Handles the vector window.

    Classes
    ----------
    UiVectorConfig(QFrame)
        The vector window which handles the adding, editing, and deleting
        of vectors and their descriptions.
"""

__author__ = "Team Keikaku"

__version__ = "1.0"

import os
import uuid

from PyQt5.QtWidgets import QApplication, QFrame, QTableWidget, QPushButton, QTableWidgetItem
from PyQt5.uic import loadUi
from definitions import UI_PATH
from src.model import vector


class UiVectorConfig(QFrame):
    """The vector window which handles the adding, editing, and deleting
    of vectors and their descriptions.
    """

    rowPosition: int

    def __init__(self):
        """Initialize the vector window and set all signals and slots
        associated with it.
        """

        super(UiVectorConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'vector_config.ui'), self)

        self.iconTable = self.findChild(QTableWidget, 'vectorTable')
        # self.iconTable.setColumnHidden(0, True)
        self.iconTable.setColumnWidth(1, 120)
        self.rowPosition = self.iconTable.rowCount()

        self.addButton = self.findChild(QPushButton, 'addVectorButton')
        self.addButton.clicked.connect(self.__add_vector)
        self.deleteButton = self.findChild(QPushButton, 'deleteVectorButton')
        self.deleteButton.clicked.connect(self.__delete_vector)

        # reconstruct vector table.
        for vector_id, v in vector.vectors.items():
            print(vector_id, v)
            self.iconTable.insertRow(self.rowPosition)
            print(self.rowPosition)
            print(vector_id)
            print(v.name)
            print(v.description)
            self.iconTable.setItem(self.rowPosition, 0, QTableWidgetItem(vector_id))
            self.iconTable.setItem(self.rowPosition, 1, QTableWidgetItem(v.name))
            self.iconTable.setItem(self.rowPosition, 2, QTableWidgetItem(v.description))
            self.rowPosition += 1

        self.iconTable.itemChanged.connect(self.__update_cell)

        self.show()

    def __add_vector(self):
        """Adds a vector to the vector table and to the vector dictionary."""

        self.iconTable.blockSignals(True)
        self.iconTable.insertRow(self.rowPosition)
        new_uuid = uuid.uuid4().__str__()
        vector.add_vector(new_uuid, 'New Vector')
        self.iconTable.setItem(self.rowPosition, 0, QTableWidgetItem(new_uuid))
        self.iconTable.setItem(self.rowPosition, 1, QTableWidgetItem('New Vector'))
        self.rowPosition += 1
        self.iconTable.blockSignals(False)

    def __delete_vector(self):
        """Removes the selected vector from the vector table and from the vector dictionary."""

        self.iconTable.blockSignals(True)
        if self.iconTable.selectionModel().hasSelection():
            rows = self.iconTable.selectionModel().selectedRows()
            indexes = []
            for row in rows:
                indexes.append(row.row())
            indexes = sorted(indexes, reverse=True)
            for rowid in indexes:
                vector.delete_vector(self.iconTable.item(rowid, 0).text())
                self.iconTable.removeRow(rowid)
                self.rowPosition -= 1
        self.iconTable.blockSignals(False)

    def __update_cell(self, item: QTableWidgetItem):
        """Updates the vector information from the cell that was just edited."""

        if item.column() == 1:
            vector.edit_vector_name(self.iconTable.item(item.row(), 0).text(), item.text())
        elif item.column() == 2:
            vector.edit_vector_desc(self.iconTable.item(item.row(), 0).text(), item.text())
        else:
            print('Invalid column')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiVectorConfig()
    app.exec_()

"""vector_config.py: Handles the vector window.

    Classes
    ----------
    UiVectorConfig(QFrame)
        The vector window which handles the adding, editing, and deleting
        of vectors and their descriptions.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

import os
from PyQt5.QtWidgets import QApplication, QFrame, QTableWidget, QPushButton
from PyQt5.uic import loadUi
from definitions import UI_PATH


class UiVectorConfig(QFrame):
    """The vector window which handles the adding, editing, and deleting
    of vectors and their descriptions.
    """

    def __init__(self):
        """Initialize the vector window and set all signals and slots
        associated with it.
        """

        super(UiVectorConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'vector_config.ui'), self)

        self.vectorTable = self.findChild(QTableWidget, 'vectorTable')
        self.vectorTable.setColumnWidth(0, 120)
        self.vectorTable.setColumnWidth(1, 120)

        self.show()

        self.addVectorButton = self.findChild(QPushButton, 'addVectorButton')
        self.addVectorButton.setShortcut("Ctrl+Return")
        self.addVectorButton.clicked.connect(self.__add_row)
        self.deleteVectorButton = self.findChild(QPushButton, 'deleteVectorButton')
        self.deleteVectorButton.setShortcut("Ctrl+Backspace")
        self.deleteVectorButton.clicked.connect(self.__delete_row)

    def __add_row(self):
        """Insert new vector entry on vector table"""

        row_position = self.vectorTable.rowCount()
        self.vectorTable.insertRow(row_position)


    def __delete_row(self):
        """Remove selected table entry from vector table"""

        indexes = self.vectorTable.selectionModel().selectedRows()
        if indexes is not None:
            for index in sorted(indexes):
                self.vectorTable.removeRow(index.row())



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiVectorConfig()
    app.exec_()

"""relationship_config.py: Handles the relationship window.

    Classes
    ----------
    UiRelationshipConfig(QFrame)
        The relationship window which handles the relationship table
        for the active vector.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

import os
from PyQt5.QtWidgets import QApplication, QFrame, QTableWidget, QPushButton
from PyQt5.uic import loadUi
from definitions import UI_PATH


class UiRelationshipConfig(QFrame):
    """The relationship window which handles the relationship table
    for the active vector.

    Attributes
    ----------
    rowPosition : int
        The index of the last row on the relation table.
    """

    rowPosition: int

    def __init__(self):
        """Initialize the relationship window and set all signals and slots
        associated with it.
        """

        super(UiRelationshipConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'relationship_config.ui'), self)

        self.relationshipTable = self.findChild(QTableWidget, 'relationshipTable')
        self.relationshipTable.resizeColumnsToContents()
        self.rowPosition = self.relationshipTable.rowCount()

        self.addRelationButton = self.findChild(QPushButton, 'addRelationButton')
        self.addRelationButton.setShortcut("Ctrl+Return")
        self.addRelationButton.clicked.connect(self.__add_relation)
        self.deleteRelationButton = self.findChild(QPushButton, 'deleteRelationButton')
        self.deleteRelationButton.setShortcut("Ctrl+Backspace")
        self.deleteRelationButton.clicked.connect(self.__delete_relation)

        self.show()

    def __add_relation(self):
        """Adds a relation to the relation table and to the relation dictionary."""

        self.relationshipTable.blockSignals(True)
        self.relationshipTable.insertRow(self.rowPosition)
        # new_uuid = uuid.uuid4().__str__()
        # TODO: add relation to relation dictionary
        self.rowPosition += 1
        self.relationshipTable.blockSignals(False)

    def __delete_relation(self):
        """Removes the selected relation from the relation table and from the relation dictionary."""

        self.relationshipTable.blockSignals(True)
        if self.relationshipTable.selectionModel().hasSelection():
            rows = self.relationshipTable.selectionModel().selectedRows()
            indexes = []
            for row in rows:
                indexes.append(row.row())
            indexes = sorted(indexes, reverse=True)
            for rowid in indexes:
                # TODO: remove relation from relation dictionary
                self.relationshipTable.removeRow(rowid)
                self.rowPosition -= 1
        self.relationshipTable.blockSignals(False)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiRelationshipConfig()
    app.exec_()

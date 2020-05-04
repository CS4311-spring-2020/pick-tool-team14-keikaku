"""relationship_config.py: Handles the relationship window.

    Classes
    ----------
    UiRelationshipConfig(QFrame)
        The relationship window which handles the relationship table
        for the active vector.
"""

__author__ = "Team Keikaku"
__version__ = "0.8"

import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFrame, QTableWidget, QPushButton, QTableWidgetItem
from PyQt5.uic import loadUi

from definitions import UI_PATH
from src.model.vector import Vector


class UiRelationshipConfig(QFrame):
    """The relationship window which handles the relationship table
    for the active vector.

    Attributes
    ----------
    rowPosition: int
        The index of the last row on the relation table.
    vector: Vector
        The vector for whom to display its relationship table.
    """

    rowPosition: int
    vector: Vector

    def __init__(self, vector: Vector):
        """Initialize the relationship window and set all signals and slots
        associated with it.

        :param vector: Vector
            The vector for whom to display its relationship table.
        """

        super(UiRelationshipConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'relationship_config.ui'), self)

        self.relationshipTable = self.findChild(QTableWidget, 'relationshipTable')
        # self.relationshipTable.setColumnHidden(0, True)
        self.relationshipTable.resizeColumnsToContents()

        self.addRelationButton = self.findChild(QPushButton, 'addRelationButton')
        self.addRelationButton.setShortcut("Ctrl+Return")
        self.addRelationButton.clicked.connect(self.__add_relation)
        self.deleteRelationButton = self.findChild(QPushButton, 'deleteRelationButton')
        self.deleteRelationButton.setShortcut("Ctrl+Backspace")
        self.deleteRelationButton.clicked.connect(self.__delete_relation)

        # self.vector = vector
        if vector:
            self.construct_relationship_table(vector)

        self.show()

    def construct_relationship_table(self, vector: Vector):
        """Constructs the relationship table for the active vector.

        :param vector: Vector
            The vector for whom to display its relationship table.
        """
        self.relationshipTable.blockSignals(True)
        self.vector = vector
        self.relationshipTable.setRowCount(0)
        self.rowPosition = 0
        # print('Constructing relationship table for: ' + str(vector.name))
        for relationship_id, relationship in vector.relationship_items():
            self.relationshipTable.insertRow(self.rowPosition)
            item = QTableWidgetItem(relationship_id)
            item.setFlags(item.flags() ^ (Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            self.relationshipTable.setItem(self.rowPosition, 0, item)
            self.relationshipTable.setItem(self.rowPosition, 1, QTableWidgetItem(relationship.parent))
            self.relationshipTable.setItem(self.rowPosition, 2, QTableWidgetItem(relationship.child))
            self.relationshipTable.setItem(self.rowPosition, 2, QTableWidgetItem(relationship.label))
            self.rowPosition += 1
        self.relationshipTable.blockSignals(False)

    def clear(self):
        """Clears the relationship table."""

        self.vector = None
        self.relationshipTable.setRowCount(0)
        self.rowPosition = 0

    def __add_relation(self):
        """Adds a relation to the relation table and to the relation dictionary."""

        self.relationshipTable.blockSignals(True)
        self.relationshipTable.insertRow(self.rowPosition)
        uid = self.vector.add_relationship()
        item = QTableWidgetItem(uid)
        item.setFlags(item.flags() ^ (Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
        self.relationshipTable.setItem(self.rowPosition, 0, item)
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
                self.vector.delete_relationship(self.relationshipTable.item(rowid, 0).text())
                self.relationshipTable.removeRow(rowid)
                self.rowPosition -= 1
        self.relationshipTable.blockSignals(False)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiRelationshipConfig()
    app.exec_()

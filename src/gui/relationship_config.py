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
from PyQt5.QtWidgets import QApplication, QFrame, QTableWidget, QWidget, QCheckBox, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from definitions import UI_PATH


class UiRelationshipConfig(QFrame):
    """The relationship window which handles the relationship table
    for the active vector.
    """

    def __init__(self):
        """Initialize the relationship window and set all signals and slots
        associated with it.
        """

        super(UiRelationshipConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'relationship_config.ui'), self)

        self.relationshipTable = self.findChild(QTableWidget, 'relationshipTable')
        self.relationshipTable.resizeColumnsToContents()

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiRelationshipConfig()
    app.exec_()

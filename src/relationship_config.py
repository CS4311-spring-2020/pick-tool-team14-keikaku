"""relationship_config.py: Handles the relationship window.

    Classes
    ----------
    UiRelationshipConfig(QFrame)
        The relationship window which handles the relationship table
        for the active vector.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

from PyQt5.QtWidgets import QApplication, QFrame, QTableWidget, QWidget, QCheckBox, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


class UiRelationshipConfig(QFrame):
    """The relationship window which handles the relationship table
    for the active vector.
    """

    def __init__(self):
        """Initialize the relationship window and set all signals and slots
        associated with it.
        """

        super(UiRelationshipConfig, self).__init__()
        loadUi('../ui/relationship_config.ui', self)

        self.relationshipTable = self.findChild(QTableWidget, 'relationshipTable')
        self.relationshipTable.resizeColumnsToContents()

        for row in range(self.relationshipTable.rowCount()):
            cell_widget = QWidget()
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.Unchecked)
            layout = QHBoxLayout(cell_widget)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            self.relationshipTable.setCellWidget(row, 0, cell_widget)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiRelationshipConfig()
    app.exec_()

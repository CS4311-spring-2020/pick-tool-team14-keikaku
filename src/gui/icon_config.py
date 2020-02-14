"""icon_config.py: Handles the icon window.

    Classes
    ----------
    UiIconConfig(QDialog)
        Initialize the icon window and set all signals and slots
        associated with it.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QWidget, QCheckBox, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


class UiIconConfig(QDialog):
    """The icon window which handles icon settings for the system."""

    def __init__(self):
        """Initialize the icon window and set all signals and slots
        associated with it.
        """

        super(UiIconConfig, self).__init__()
        loadUi('../ui/icon_config.ui', self)

        self.iconTable = self.findChild(QTableWidget, 'iconTable')
        self.iconTable.setColumnWidth(0, 30)
        self.iconTable.setColumnWidth(1, 120)
        self.iconTable.setColumnWidth(2, 120)

        for row in range(self.iconTable.rowCount()):
            cell_widget = QWidget()
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.Unchecked)
            layout = QHBoxLayout(cell_widget)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            self.iconTable.setCellWidget(row, 0, cell_widget)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiIconConfig()
    app.exec_()

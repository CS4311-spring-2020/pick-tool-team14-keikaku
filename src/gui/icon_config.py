"""icon_config.py: Handles the icon window.

    Classes
    ----------
    UiIconConfig(QDialog)
        Initialize the icon window and set all signals and slots
        associated with it.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

import os

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget
from PyQt5.uic import loadUi

from definitions import UI_PATH


class UiIconConfig(QDialog):
    """The icon window which handles icon settings for the system."""

    def __init__(self):
        """Initialize the icon window and set all signals and slots
        associated with it.
        """

        super(UiIconConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'icon_config.ui'), self)

        self.iconTable = self.findChild(QTableWidget, 'iconTable')
        self.iconTable.setColumnWidth(0, 30)
        self.iconTable.setColumnWidth(1, 120)
        self.iconTable.setColumnWidth(2, 120)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiIconConfig()
    app.exec_()

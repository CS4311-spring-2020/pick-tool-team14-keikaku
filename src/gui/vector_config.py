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
from PyQt5.QtWidgets import QApplication, QFrame, QTableWidget
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

        self.iconTable = self.findChild(QTableWidget, 'vectorTable')
        self.iconTable.setColumnWidth(0, 120)
        self.iconTable.setColumnWidth(1, 120)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiVectorConfig()
    app.exec_()

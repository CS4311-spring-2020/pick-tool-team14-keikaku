"""export_config.py: Handles the export window.

    Classes
    ----------
    UiExportConfig(QDialog)
        The export window which handles exporting vector and entry
        data to an external file.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

import os
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from definitions import UI_PATH


class UiExportConfig(QDialog):
    """The export window which handles exporting vector and entry
    data to an external file.
    """

    def __init__(self):
        """Initialize the export window and set all signals and slots
        associated with it.
        """

        super(UiExportConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'export_config.ui'), self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiExportConfig()
    app.exec_()

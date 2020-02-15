"""change_config.py: Handles the commit window.

    Classes
    ----------
    UiChangeConfig(QDialog)
        The commit window which handles the committing of log entry
        and vector changes.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

import os
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from definitions import UI_PATH


class UiChangeConfig(QDialog):
    """The commit window which handles the committing of log entry
    and vector changes.
    """

    def __init__(self):
        """Initialize the commit window and set all signals and slots
        associated with it.
        """

        super(UiChangeConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'change_config.ui'), self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiChangeConfig()
    app.exec_()

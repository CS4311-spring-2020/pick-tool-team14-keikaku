"""change_config.py: Handles the commit window.

    Classes
    ----------
    UiChangeConfig(QDialog)
        The commit window which handles the committing of log entry
        and vector changes.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class UiChangeConfig(QDialog):
    """The commit window which handles the committing of log entry
    and vector changes.
    """

    def __init__(self):
        """Initialize the commit window and set all signals and slots
        associated with it.
        """

        super(UiChangeConfig, self).__init__()
        loadUi('../ui/change_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiChangeConfig()
    app.exec_()

"""icon_config.py: Handles the icon window.

    Classes
    ----------
    UiIconConfig(QDialog)
        Initialize the icon window and set all signals and slots
        associated with it.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class UiIconConfig(QDialog):
    """The icon window which handles icon settings for the system."""

    def __init__(self):
        """Initialize the icon window and set all signals and slots
        associated with it.
        """

        super(UiIconConfig, self).__init__()
        loadUi('../ui/icon_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiIconConfig()
    app.exec_()

"""directory_config.py: Handles the directory window.

    Classes
    ----------
    UiDirectoryConfig(QDialog)
        The directory window which handles the setting of
        file directory paths.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class UiDirectoryConfig(QDialog):
    """The directory window which handles the setting of
    file directory paths.
    """

    def __init__(self):
        """Initialize the directory window and set all signals and slots
        associated with it.
        """

        super(UiDirectoryConfig, self).__init__()
        loadUi('../ui/directory_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiDirectoryConfig()
    app.exec_()

"""filter_config.py: Handles the filter window.

    Classes
    ----------
    UiFilterConfig(QDialog)
        The filter window which handles the creation and application of a
        search filter.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class UiFilterConfig(QDialog):
    """The filter window which handles the creation and application of a
    search filter.
    """

    def __init__(self):
        """Initialize the filter window and set all signals and slots
        associated with it.
        """

        super(UiFilterConfig, self).__init__()
        loadUi('../ui/filter_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiFilterConfig()
    app.exec_()

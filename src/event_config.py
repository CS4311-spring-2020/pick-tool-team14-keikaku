"""event_config.py: Handles the event window.

    Classes
    ----------
    UiEventConfig(QDialog)
        The event window which handles the setting of
        project event information.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class UiEventConfig(QDialog):
    """The event window which handles the setting of
    project event information.
    """

    def __init__(self):
        """Initialize the event window and set all signals and slots
        associated with it.
        """

        super(UiEventConfig, self).__init__()
        loadUi('../ui/event_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiEventConfig()
    app.exec_()

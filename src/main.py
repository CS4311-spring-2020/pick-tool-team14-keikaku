"""main.py: Entry point of the program.
    Handles program entry and exit routines.
"""

__author__ = "Team Keikaku"
__version__ = "1.0"

import atexit

from PyQt5.QtWidgets import QApplication

from src.gui.main_ui import Ui
from src.model import settings, event

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Ui()
    event.load()
    settings.load()
    app.exec_()


@atexit.register
def save():
    settings.save()

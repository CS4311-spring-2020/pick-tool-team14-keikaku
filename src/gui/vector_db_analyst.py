"""vector_db_analyst.py: Handles the analysts's vector db window.

    Classes
    ----------
    UiVectorDBAnalyst(QFrame)
        The analyst vector db window which handles the pulling and pushing
        of vector changes between the analyst and host systems.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

import os

from PyQt5.QtWidgets import QApplication, QFrame
from PyQt5.uic import loadUi

from definitions import UI_PATH


class UiVectorDBAnalyst(QFrame):
    """The analyst vector db window which handles the pulling and pushing
    of vector changes between the analyst and host systems.
    """

    def __init__(self):
        """Initialize the analyst vector db window and set all signals and slots
        associated with it.
        """

        super(UiVectorDBAnalyst, self).__init__()
        loadUi(os.path.join(UI_PATH, 'vector_db_analyst.ui'), self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiVectorDBAnalyst()
    app.exec_()

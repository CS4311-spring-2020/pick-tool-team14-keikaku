"""vector_db_lead.py: Handles the lead's vector db window.

    Classes
    ----------
    UiVectorDBLead(QFrame)
        The lead vector db window which handles the accepting of queued
        analyst push requests.
"""

__author__ = "Team Keikaku"

__version__ = "0.1"

import os
from PyQt5.QtWidgets import QApplication, QFrame
from PyQt5.uic import loadUi
from definitions import UI_PATH


class UiVectorDBLead(QFrame):
    """The lead vector db window which handles the accepting of queued
    analyst push requests.
    """

    def __init__(self):
        """Initialize the lead vector db window and set all signals and slots
        associated with it.
        """

        super(UiVectorDBLead, self).__init__()
        loadUi(os.path.join(UI_PATH, 'vector_db_lead.ui'), self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiVectorDBLead()
    app.exec_()

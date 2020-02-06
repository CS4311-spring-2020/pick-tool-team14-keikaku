"""team_config.py: Handles the team window.

    Classes
    ----------
    UiTeamConfig(QDialog)
        The team window which handles the system role and connections
        to the host when running as a client.
"""

__author__ = "Team Keikaku"

__version__ = "0.2"

from PyQt5.QtWidgets import QApplication, QDialog, QCheckBox, QLabel, QLineEdit
from PyQt5.uic import loadUi
from src import settings


class UiTeamConfig(QDialog):
    """The team window which handles the system role and connections
    to the host when running as a client.
    """

    def __init__(self):
        """Initialize the team window and set all signals and slots
        associated with it.
        """

        super(UiTeamConfig, self).__init__()
        loadUi('../ui/team_config.ui', self)

        self.leadCheckBox = self.findChild(QCheckBox, 'leadCheckBox')
        self.leadCheckBox.setCheckState(settings.lead_status)
        self.leadCheckBox.stateChanged.connect(self.__toggle_lead)
        self.leadIPLabel = self.findChild(QLabel, 'leadIPLabel')
        self.leadIPText = self.findChild(QLineEdit, 'leadIPText')
        if settings.lead_status:
            self.leadIPLabel.setEnabled(False)
            self.leadIPText.setEnabled(False)

        self.show()

    def __toggle_lead(self):
        """Toggle the host IP label and text line, then toggle lead_status."""

        self.leadIPLabel.setEnabled(not self.leadIPLabel.isEnabled())
        self.leadIPText.setEnabled(not self.leadIPText.isEnabled())
        settings.toggle_lead()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiTeamConfig()
    app.exec_()

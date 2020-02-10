"""team_config.py: Handles the team window.

    Classes
    ----------
    UiTeamConfig(QDialog)
        The team window which handles the system role and connections
        to the host when running as a client.
"""

__author__ = "Team Keikaku"

__version__ = "0.3"

from PyQt5.QtWidgets import QApplication, QDialog, QCheckBox, QLabel, QLineEdit, QPushButton
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
        self.connectButton = self.findChild(QPushButton, 'connectButton')
        self.yourIPLabel = self.findChild(QLabel, 'yourIPLabel')
        self.yourIPText = self.findChild(QLineEdit, 'yourIPText')
        if settings.lead_status:
            self.leadIPLabel.setEnabled(False)
            self.leadIPText.setEnabled(False)
            self.connectButton.setEnabled(False)
        else:
            self.yourIPLabel.setEnabled(False)
            self.yourIPText.setEnabled(False)

        self.yourIPText = self.findChild(QLineEdit, 'yourIPText')
        self.yourIPText.insert(settings.host_ip_address)
        self.yourIPText.editingFinished.connect(self.__set_host_ip)

        self.leadIPText = self.findChild(QLineEdit, 'leadIPText')
        self.leadIPText.insert(settings.target_ip_address)
        self.leadIPText.editingFinished.connect(self.__set_target_ip)

        self.show()

    def __toggle_lead(self):
        """Toggle the host IP label, text line, and connect button;
        then toggle lead_status.
        """

        self.leadIPLabel.setEnabled(not self.leadIPLabel.isEnabled())
        self.leadIPText.setEnabled(not self.leadIPText.isEnabled())
        self.connectButton.setEnabled(not self.connectButton.isEnabled())
        self.yourIPLabel.setEnabled(not self.yourIPLabel.isEnabled())
        self.yourIPText.setEnabled(not self.yourIPText.isEnabled())
        settings.toggle_lead()

    def __set_host_ip(self):
        """Sets the target_ip_address to yourIPText's text."""

        settings.host_ip_address = self.yourIPText.text()

    def __set_target_ip(self):
        """Sets the target_ip_address to leadIPText's text."""

        settings.target_ip_address = self.leadIPText.text()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiTeamConfig()
    app.exec_()

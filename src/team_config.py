from PyQt5.QtWidgets import QApplication, QDialog, QCheckBox
from PyQt5.uic import loadUi

lead_status = 0


def toggle_lead():
    global lead_status
    lead_status = lead_status ^ 2


class UiTeamConfig(QDialog):
    def __init__(self):
        super(UiTeamConfig, self).__init__()
        loadUi('../ui/team_config.ui', self)

        self.leadCheckBox.setCheckState(lead_status)
        self.leadCheckBox = self.findChild(QCheckBox, 'leadCheckBox')
        self.leadCheckBox.stateChanged.connect(toggle_lead)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiTeamConfig()
    app.exec_()

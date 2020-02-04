from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class UiTeamConfig(QDialog):
    def __init__(self):
        super(UiTeamConfig, self).__init__()
        loadUi('../ui/team_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiTeamConfig()
    app.exec_()

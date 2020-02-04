from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class UiChangeConfig(QDialog):
    def __init__(self):
        super(UiChangeConfig, self).__init__()
        loadUi('../ui/change_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiChangeConfig()
    app.exec_()

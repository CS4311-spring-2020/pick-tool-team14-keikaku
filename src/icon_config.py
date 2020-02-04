from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class UiIconConfig(QDialog):
    def __init__(self):
        super(UiIconConfig, self).__init__()
        loadUi('../ui/icon_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiIconConfig()
    app.exec_()

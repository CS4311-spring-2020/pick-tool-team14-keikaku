from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class UiDirectoryConfig(QDialog):
    def __init__(self):
        super(UiDirectoryConfig, self).__init__()
        loadUi('../ui/directory_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiDirectoryConfig()
    app.exec_()

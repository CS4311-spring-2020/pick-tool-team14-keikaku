from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class UiExportConfig(QDialog):
    def __init__(self):
        super(UiExportConfig, self).__init__()
        loadUi('../ui/export_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiExportConfig()
    app.exec_()

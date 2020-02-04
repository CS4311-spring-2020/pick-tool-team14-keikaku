from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class UiFilterConfig(QDialog):
    def __init__(self):
        super(UiFilterConfig, self).__init__()
        loadUi('../ui/filter_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiFilterConfig()
    app.exec_()

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class UiEventConfig(QDialog):
    def __init__(self):
        super(UiEventConfig, self).__init__()
        loadUi('../ui/event_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiEventConfig()
    app.exec_()

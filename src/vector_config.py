from PyQt5.QtWidgets import QApplication, QFrame
from PyQt5.uic import loadUi


class UiVectorConfig(QFrame):
    def __init__(self):
        super(UiVectorConfig, self).__init__()
        loadUi('../ui/vector_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiVectorConfig()
    app.exec_()

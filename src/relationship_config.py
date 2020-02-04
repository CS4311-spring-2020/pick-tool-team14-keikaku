from PyQt5.QtWidgets import QApplication, QFrame
from PyQt5.uic import loadUi


class UiRelationshipConfig(QFrame):
    def __init__(self):
        super(UiRelationshipConfig, self).__init__()
        loadUi('../ui/relationship_config.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiRelationshipConfig()
    app.exec_()

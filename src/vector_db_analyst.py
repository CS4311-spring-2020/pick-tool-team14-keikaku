from PyQt5.QtWidgets import QApplication, QFrame
from PyQt5.uic import loadUi


class UiVectorDBAnalyst(QFrame):
    def __init__(self):
        super(UiVectorDBAnalyst, self).__init__()
        loadUi('../ui/vector_db_analyst.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiVectorDBAnalyst()
    app.exec_()

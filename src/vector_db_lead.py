from PyQt5.QtWidgets import QApplication, QFrame
from PyQt5.uic import loadUi


class UiVectorDBLead(QFrame):
    def __init__(self):
        super(UiVectorDBLead, self).__init__()
        loadUi('../ui/vector_db_lead.ui', self)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiVectorDBLead()
    app.exec_()

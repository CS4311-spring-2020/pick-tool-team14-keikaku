import os

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QMessageBox
from PyQt5.uic import loadUi

from definitions import UI_PATH
from src.model.splunk import SplunkManager


class UiSplunkConfig(QDialog):
    """The splunk window which handles connection.

    start_ingestion: pyqtSignal
        A pyQT signal emitted when connection established.
    """

    connected = pyqtSignal(object)

    def __init__(self):
        """Initialize the directory window and set all signals and slots
        associated with it.
        """

        super(UiSplunkConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'splunk_config.ui'), self)

        self.hostLineEdit = self.findChild(QLineEdit, 'hostLineEdit')
        self.portLineEdit = self.findChild(QLineEdit, 'portLineEdit')
        self.usernameLineEdit = self.findChild(QLineEdit, 'usernameLineEdit')
        self.passwordLineEdit = self.findChild(QLineEdit, 'passwordLineEdit')

        self.connectButton = self.findChild(QPushButton, 'connectButton')
        self.connectButton.clicked.connect(self.__connect)
        self.msg = QMessageBox()

        self.show()

    def __connect(self):
        """Connects to Splunk."""

        if not self.hostLineEdit.text() or not self.portLineEdit.text() or not self.usernameLineEdit.text():
            self.msg.setText("<font color='red'>Host or Description or Username is empty!</font>")

        else:
            splunk_manage = SplunkManager()
            splunk_connection = splunk_manage.connect(self.hostLineEdit.text(),
                                                           self.portLineEdit.text(),
                                                           self.usernameLineEdit.text(),
                                                           self.passwordLineEdit.text())

            if not splunk_connection:
                self.msg.setText("<font color='green'>Connection Established!</font>")
                self.connected.emit(splunk_manage)

            else:
                self.msg.setText(f"<font color='red'>{splunk_connection}!</font>")
                self.connected.emit(None)

        self.msg.exec()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiSplunkConfig()
    app.exec_()

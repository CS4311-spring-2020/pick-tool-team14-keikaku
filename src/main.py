from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi
from src.change_config import UiChangeConfig
from src.directory_config import UiDirectoryConfig
from src.event_config import UiEventConfig
from src.export_config import UiExportConfig
from src.filter_config import UiFilterConfig
from src.icon_config import UiIconConfig
from src.relationship_config import UiRelationshipConfig
from src.team_config import UiTeamConfig
from src.vector_config import UiVectorConfig
from src.vector_db_analyst import UiVectorDBAnalyst
from src.vector_db_lead import UiVectorDBLead


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        loadUi('../ui/main_window.ui', self)

        self.teamButton = self.findChild(QPushButton, 'teamButton')
        self.teamButton.clicked.connect(self.execute_team_config)
        self.teamButton = self.findChild(QPushButton, 'eventButton')
        self.teamButton.clicked.connect(self.execute_event_config)
        self.teamButton = self.findChild(QPushButton, 'vectorButton')
        self.teamButton.clicked.connect(self.execute_vector_config)
        self.teamButton = self.findChild(QPushButton, 'filterButton')
        self.teamButton.clicked.connect(self.execute_filter_config)
        self.teamButton = self.findChild(QPushButton, 'commitButton')
        self.teamButton.clicked.connect(self.execute_change_config)
        self.teamButton = self.findChild(QPushButton, 'syncButton')
        if True:  # TODO: Find lead checkbox state
            self.teamButton.clicked.connect(self.execute_vector_analyst)
        else:
            self.teamButton.clicked.connect(self.execute_vector_analyst)
        self.teamButton = self.findChild(QPushButton, 'exportButton')
        self.teamButton.clicked.connect(self.execute_export_config)
        self.teamButton = self.findChild(QPushButton, 'directoryButton')
        self.teamButton.clicked.connect(self.execute_directory_config)
        self.teamButton = self.findChild(QPushButton, 'iconButton')
        self.teamButton.clicked.connect(self.execute_icon_config)
        self.teamButton = self.findChild(QPushButton, 'relationshipsButton')
        self.teamButton.clicked.connect(self.execute_relationship_config)

        self.show()

    def execute_change_config(self):
        self.window = UiChangeConfig()
        self.window.show()

    def execute_directory_config(self):
        self.window = UiDirectoryConfig()
        self.window.show()

    def execute_event_config(self):
        self.window = UiEventConfig()
        self.window.show()

    def execute_export_config(self):
        self.window = UiExportConfig()
        self.window.show()

    def execute_filter_config(self):
        self.window = UiFilterConfig()
        self.window.show()

    def execute_icon_config(self):
        self.window = UiIconConfig()
        self.window.show()

    def execute_relationship_config(self):
        self.window = UiRelationshipConfig()
        self.window.show()

    def execute_team_config(self):
        self.window = UiTeamConfig()
        self.window.show()

    def execute_vector_config(self):
        self.window = UiVectorConfig()
        self.window.show()

    def execute_vector_analyst(self):
        self.window = UiVectorDBAnalyst()
        self.window.show()

    def execute_vector_lead(self):
        self.window = UiVectorDBLead()
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Ui()
    app.exec_()

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox
from PyQt5.uic import loadUi
from src import team_config
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
        self.eventButton = self.findChild(QPushButton, 'eventButton')
        self.eventButton.clicked.connect(self.execute_event_config)
        self.vectorButton = self.findChild(QPushButton, 'vectorButton')
        self.vectorButton.clicked.connect(self.execute_vector_config)
        self.filterButton = self.findChild(QPushButton, 'filterButton')
        self.filterButton.clicked.connect(self.execute_filter_config)
        self.commitButton = self.findChild(QPushButton, 'commitButton')
        self.commitButton.clicked.connect(self.execute_change_config)
        self.syncButton = self.findChild(QPushButton, 'syncButton')
        self.syncButton.clicked.connect(self.execute_vector_db)
        self.exportButton = self.findChild(QPushButton, 'exportButton')
        self.exportButton.clicked.connect(self.execute_export_config)
        self.directoryButton = self.findChild(QPushButton, 'directoryButton')
        self.directoryButton.clicked.connect(self.execute_directory_config)
        self.iconButton = self.findChild(QPushButton, 'iconButton')
        self.iconButton.clicked.connect(self.execute_icon_config)
        self.relationshipButton = self.findChild(QPushButton, 'relationshipsButton')
        self.relationshipButton.clicked.connect(self.execute_relationship_config)

        self.show()

    def execute_change_config(self):
        self.change_window = UiChangeConfig()
        self.change_window.show()

    def execute_directory_config(self):
        self.directory_window = UiDirectoryConfig()
        self.directory_window.show()

    def execute_event_config(self):
        self.event_window = UiEventConfig()
        self.event_window.show()

    def execute_export_config(self):
        self.export_window = UiExportConfig()
        self.export_window.show()

    def execute_filter_config(self):
        self.filter_window = UiFilterConfig()
        self.filter_window.show()

    def execute_icon_config(self):
        self.icon_window = UiIconConfig()
        self.icon_window.show()

    def execute_relationship_config(self):
        self.relationship_window = UiRelationshipConfig()
        self.relationship_window.show()

    def execute_team_config(self):
        self.team_window = UiTeamConfig()
        self.team_window.show()

    def execute_vector_config(self):
        self.vector_window = UiVectorConfig()
        self.vector_window.show()

    def execute_vector_db(self):
        if team_config.lead_status:
            self.vector_db_window = UiVectorDBLead()
        else:
            self.vector_db_window = UiVectorDBAnalyst()
        self.vector_db_window.show()

    def execute_vector_analyst(self):
        self.vector_analyst_window = UiVectorDBAnalyst()
        self.vector_analyst_window.show()

    def execute_vector_lead(self):
        self.vector_lead_window = UiVectorDBLead()
        self.vector_lead_window.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Ui()
    app.exec_()

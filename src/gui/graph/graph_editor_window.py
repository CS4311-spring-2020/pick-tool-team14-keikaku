import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile

from src.gui.graph.attack_graph_scene import AttackGraphScence
from src.gui.graph.attack_graph_view import AttackGraphView
from src.gui.graph.node_scene import NodeScene
from src.gui.graph.node_module import NodeModule

class GraphEditorWindow(QWidget):
    """
    Temporary class windows used to develop the attack graph scene.
    Once the attack graph feature is complete all usability will be transferred
    to the main GUI class.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.style_sheet_filename = "qss/nodestyle.qss"
        self.load_style_sheet()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(200, 200, 800, 600)

        # Stretches graphics view
        self.layout = QVBoxLayout()

        # Removes content margins
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Create graphics scene
        # TODO change so that it isn't reliant on gr_scene pointer
        self.scene = NodeScene()
        # self.gr_scene = self.scene.gr_scene

        node = NodeModule(self.scene, "Node Name")

        # Create graphics view
        self.view = AttackGraphView(self.scene.gr_scene, self)
        self.layout.addWidget(self.view)


        self.setWindowTitle("Graph Editor")
        self.show()

    def load_style_sheet(self):
        file = QFile(self.style_sheet_filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll()
        QApplication.instance().setStyleSheet(str(stylesheet, encoding="utf-8"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = GraphEditorWindow()

    sys.exit(app.exec_())

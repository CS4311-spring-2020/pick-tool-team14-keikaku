import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QApplication
from src.gui.graph.attack_graph_scene import AttackGraphScence

class GraphEditorWindow(QWidget):
    """
    Temporary class windows used to develop the attack graph scene.
    Once the attack graph feature is complete all usability will be transferred
    to the main GUI class.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(200, 200, 200, 600)

        # Stretches graphics view
        self.layout = QVBoxLayout()
        # Removes content margins
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Create graphics scene
        self.grScence = AttackGraphScence()

        # Create graphics view
        self.view = QGraphicsView(self)
        self.view.setScene(self.grScence)
        self.layout.addWidget(self.view)

        self.setWindowTitle("Graph Editor")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = GraphEditorWindow()

    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QApplication
from src.gui.graph.node_graphics_scene import QNodeGraphicsScence

class GraphEditorWindow(QWidget):
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
        self.grScence = QNodeGraphicsScence()

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
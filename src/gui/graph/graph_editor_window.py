import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QApplication
# Added for drawing on the window
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsItem

from src.gui.graph.attack_graph_scene import AttackGraphScence
from src.gui.graph.attack_graph_view import AttackGraphView

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
        self.setGeometry(200, 200, 800, 600)

        # Stretches graphics view
        self.layout = QVBoxLayout()

        # Removes content margins
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Create graphics scene
        self.gr_scene = AttackGraphScence()

        # Create graphics view
        self.view = AttackGraphView(self.gr_scene, self)
        self.layout.addWidget(self.view)


        self.setWindowTitle("Graph Editor")
        self.show()

        self.add_debug_content()

    def add_debug_content(self):
        # Parameters used for drawing the rectangle
        brush_pen = QBrush(Qt.green)
        outline_pen = QPen(Qt.black)
        outline_pen.setWidth(2)

        # Drawing the rectangle
        rect = self.gr_scene.addRect(-100, -100, 80, 100, outline_pen, brush_pen)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        # Inserting text
        text = self.gr_scene.addText("The is text")
        text.setFlag(QGraphicsItem.ItemIsMovable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = GraphEditorWindow()

    sys.exit(app.exec_())

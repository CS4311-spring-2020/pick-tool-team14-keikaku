import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile
from PyQt5.Qt import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QPen

from src.gui.graph.graph_editor_view import GraphEditorView
from src.gui.graph.graph_editor_scene import GraphEditorScene

class GraphEditorWindow(QWidget):
    """
    Temporary class windows used to develop the attack graph scene.
    Once the attack graph feature is complete all usability will be transferred
    to the main GUI class.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # self.style_sheet_filename = "qss/nodestyle.qss"
        # self.load_style_sheet()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(200, 200, 800, 600)

        # Creates Box layout and removes layout border (content margins)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Graph editor scene that holds all graph elements
        self.graph_editor_scene = GraphEditorScene()
        self.background_scene = self.graph_editor_scene.background_scene

        # Create the view where the graph will be displayed
        self.view = GraphEditorView(self.background_scene, self)
        self.layout.addWidget(self.view)

        self.setWindowTitle("Graph Editor")
        self.show()

        self.addDebugContent()

    def addDebugContent(self):
        brush = QBrush(Qt.red)
        outline = QPen(Qt.black)
        outline.setWidth(2)
        node = self.background_scene.addEllipse(-100, -100, 100, 100, outline, brush)
        node.setFlag(QGraphicsItem.ItemIsMovable)

    # def load_style_sheet(self):
    #     file = QFile(self.style_sheet_filename)
    #     file.open(QFile.ReadOnly | QFile.Text)
    #     stylesheet = file.readAll()
    #     QApplication.instance().setStyleSheet(str(stylesheet, encoding="utf-8"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = GraphEditorWindow()

    sys.exit(app.exec_())

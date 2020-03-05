
from PyQt5.QtCore import QDateTime
from src.gui.graph.node_graphics import NodeGraphics
from src.model.node import Node
from src.gui.graph.node_scene import NodeScene
from src.gui.graph.node_content_widget import NodeContentWidget

class NodeModule():

    def __init__(self, scene : NodeScene, name="Undefined Node"):
        self.scene = scene
        self.name = name

        self.content = NodeContentWidget()
        self.gr_node = NodeGraphics(self)

        self.scene.add_node(self)
        self.scene.gr_scene.addItem(self.gr_node)

        self.gr_node.name = name

        self.inputs = []
        self.outputs = []
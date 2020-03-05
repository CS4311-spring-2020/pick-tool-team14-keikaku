
from PyQt5.QtCore import QDateTime
from src.gui.graph.node_graphics import NodeGraphics
from src.model.node import Node
from src.gui.graph.node_scene import NodeScene
class NodeModule():

    def __init__(self, scene : NodeScene, description="Undefined Node"):
        self.scene = scene
        self.description = description
        self.gr_node = NodeGraphics(self, self.description)

        self.scene.add_node(self)
        self.scene.gr_scene.addItem(self.gr_node)

        self.gr_node.description = description

        self.inputs = []
        self.outputs = []
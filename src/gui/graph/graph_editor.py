from PyQt5.Qt import QGraphicsItemGroup
from PyQt5.Qt import QGraphicsLineItem
from PyQt5.Qt import QPen
from PyQt5.Qt import Qt
from src.gui.graph.graph_editor_scene import GraphEditorScene
from src.gui.graph.node_item import NodeItem
from src.gui.graph.relationship_item import RelationshipItem

class GraphEditor:
    vectos: dict
    nodes: dict
    relationships: dict

    def __init__(self):
        self.vectos = {}
        self.nodes = {}
        self.relationships = {}

        self.scene_width = 64000
        self.scene_height = 64000

        self.init_ui()

    def init_ui(self):
        self.graph_editor_scence = GraphEditorScene(self.scene_width, self.scene_height)
        node_1 = NodeItem(-100, -100, "Hello", "Red")
        node_2 = NodeItem(-200, -200, "Hello", "Red")
        self.graph_editor_scence.addItem(node_1)
        self.graph_editor_scence.addItem(node_2)
        relationship = RelationshipItem(node_1.name, node_2.name, node_1.center_pos(), node_2.center_pos())
        self.graph_editor_scence.addItem(relationship)
        # line_2 = QLine()

    def add_vector(self, key, vector):
        self.vectos[key] = vector

    def add_node(self, key,  node):
        self.nodes[key] = node

    def add_relationship(self, key, relationship):
        self.relationships[key] = relationship

    def remove_vector(self, key):
        self.vectos.pop(key)

    def remove_node(self, key):
        self.nodes.pop(key)

    def remove_relationship(self, key):
        self.relationships.pop(key)


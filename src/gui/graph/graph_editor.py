from PyQt5.Qt import QGraphicsItemGroup
from PyQt5.Qt import QRectF
from PyQt5.Qt import QPen
from PyQt5.Qt import Qt
from src.gui.graph.graph_editor_scene import GraphEditorScene
from src.gui.graph.node_item import NodeItem
from src.gui.graph.relationship_item import RelationshipItem
from src.gui.graph.vector_item_group import VectorItemGroup

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
        self.graph_editor_scene = GraphEditorScene(self.scene_width, self.scene_height)
        self.add_vector()
        node1 = self.add_node(-100, -100)
        node2 = self.add_node(100, 100)
        self.add_relationship(node1, node2)
        self.add_node_to_vector(node1)
        self.add_node_to_vector(node2)
        self.graph_editor_scene.addItem(node1)
        self.graph_editor_scene.addItem(node2)
        self.graph_editor_scene.addItem(self.vector.get_bound_box_item())

    def add_vector(self):
        self.vector = VectorItemGroup()

    def add_node_to_vector(self, node):
        self.vector.addToGroup(node)

    def add_node(self, x, y):
        node_item = NodeItem(x, x, "Hello", "Red")
        self.graph_editor_scene.addItem(node_item)
        return node_item

    def add_relationship(self, parent_node, child_node):
        relationship = RelationshipItem(parent_node.name, child_node.name,
                                        parent_node.center_pos(), child_node.center_pos(), parent_node)
        self.graph_editor_scene.addItem(relationship)

    def remove_vector(self, key):
        self.vectos.pop(key)

    def remove_node(self, key):
        self.nodes.pop(key)

    def remove_relationship(self, key):
        self.relationships.pop(key)


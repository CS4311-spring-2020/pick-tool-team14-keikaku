from src.gui.graph.graph_editor_scene import GraphEditorScene
from src.gui.graph.node_item import NodeItem
from src.gui.graph.relationship_item import RelationshipItem
from src.gui.graph.vector_item_group import VectorItemGroup
import time

class GraphEditor:
    '''
        This class handle the functions that will be performed on the graph editor which mostly includes adding and
        deleting items from the the GraphEditorScene

        Attributes
        ----------
        vectors : dict
            dictionary containing all the VectorItemGroups
        node : dict
            dictionary containing all the NodeItems
        relationships: dict
            dictionary containing all the RelationshipItems
        graph_editor_scene : GraphEditorScene
            The GraphEditorScene that we give the items created by this class
    '''
    vectors: dict
    nodes: dict
    relationships: dict
    graph_editor_scene : GraphEditorScene

    def __init__(self):
        self.vectors = {}
        self.nodes = {}
        self.relationships = {}

        self.scene_width = 64000
        self.scene_height = 64000

        self.init_ui()

    '''
        Initializes parameters for this class
    '''

    def init_ui(self):
        self.graph_editor_scene = GraphEditorScene(self.scene_width, self.scene_height)
        # @TODO The following is hard coded and will be automated later
        self.add_vector()
        node1 = self.add_node(-200, -200, "Test 1")
        node3 = self.add_node(-100, -100, "Test3")
        node2 = self.add_node(100, 100, "Test2")
        self.add_relationship(node1, node2, "T1->T2")
        self.add_node_to_vector(node1)
        self.add_node_to_vector(node2)
        self.graph_editor_scene.addItem(node1)
        self.graph_editor_scene.addItem(node2)
        self.graph_editor_scene.addItem(self.vector.get_bound_box_item())
        time.sleep(10)



    def add_vector(self):
        self.vector = VectorItemGroup()

    def add_node_to_vector(self, node):
        self.vector.addToGroup(node)

    def add_node(self, x, y, name :str):
        node_item = NodeItem(x, x, name, "Red")
        self.graph_editor_scene.addItem(node_item)
        return node_item

    def add_relationship(self, parent_node, child_node, name):
        relationship = RelationshipItem(parent_node.name, child_node.name, parent_node.center_pos(),
                                        child_node.center_pos(), name)
        parent_node.add_relationship(name, relationship)
        child_node.add_relationship(name, relationship)
        self.graph_editor_scene.addItem(relationship)

    def remove_vector(self, key):
        self.vectors.pop(key)

    def remove_node(self, key):
        self.nodes.pop(key)

    def remove_relationship(self, key):
        self.relationships.pop(key)


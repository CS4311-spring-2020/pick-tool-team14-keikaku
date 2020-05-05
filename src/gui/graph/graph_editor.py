from typing import Dict
from src.gui.graph.graph_editor_view import GraphEditorView
from src.gui.graph.graph_editor_scene import GraphEditorScene
from src.gui.graph.node_item import NodeItem
from src.gui.graph.relationship_item import RelationshipItem
from src.gui.graph.vector_item_group import VectorItemGroup
from src.model.vector import Vector
from src.model.node import Node
from src.model.relationship import Relationship
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
    vector_dictionary: Dict[str, VectorItemGroup] = {}
    node_dictionary: Dict[str, NodeItem] = {}
    relationship_dictionary: Dict[str, RelationshipItem] = {}
    graph_editor_view: GraphEditorView
    graph_editor_scene: GraphEditorScene
    selected_vector_item_group: VectorItemGroup

    def __init__(self, parent=None):
        self.scene_width = 64000
        self.scene_height = 64000

        self.graph_editor_scene = GraphEditorScene(self.scene_width, self.scene_height)
        self.graph_editor_view = GraphEditorView(self.graph_editor_scene, parent)
        self.init_ui()

    '''
        Initializes parameters for this class
    '''

    def init_ui(self):
        # @TODO The following is hard coded and will be automated later
        vector = Vector()
        self.add_vector(vector)
        node1 = Node(name="Test_Node1")
        node2 = Node(name="Test_Node2")
        self.add_node(node1)
        self.add_node(node2)

        relationship = Relationship(node1.name, node2.name, "Test_Relationship1")
        self.add_relationship(relationship)

    def display_vector(self, vector: Vector):
        # First check if the vector is in the dictionary if not then create it
        if vector.name in self.vector_dictionary:
            self.selected_vector_item_group = self.vector_dictionary[vector.name]
        else:
            self.add_vector(vector)
            self.selected_vector_item_group = self.vector_dictionary[vector.name]

        self.toggle_visibility(vector)

    def add_vector(self, vector: Vector):
        new_vector = VectorItemGroup(vector)
        self.graph_editor_scene.addItem(new_vector)
        self.vector_dictionary[vector.name] = new_vector
        self.selected_vector_item_group = new_vector
        self.toggle_visibility(vector)

    def toggle_visibility(self, vector: Vector):
        # Toggle the visibility of the selected VectorItemGroup and hide the others
        for vector_group in self.vector_dictionary.values():
            if vector.name == vector_group.name:
                vector_group.setVisible(True)
            else:
                vector_group.setVisible(False)

    def add_node(self, node: Node):
        # polygon = self.graph_editor_view.mapFromScene(self.graph_editor_scene.sceneRect())
        # point = polygon.boundingRect().center()
        # print(point.x(), point.y())
        # node_item = NodeItem(point.x(), point.y(), node)

        node_item = NodeItem(0, 0, node)
        self.graph_editor_scene.addItem(node_item)
        self.node_dictionary[node.name] = node_item
        self.selected_vector_item_group.add_to_list(node_item)

    def add_relationship(self, relationship: Relationship):
        # Find the nodes for this relationship in the node dictionary
        parent_node_item = self.node_dictionary[relationship.parent]
        child_node_item = self.node_dictionary[relationship.child]

        # Create the relationship
        relationship_item = RelationshipItem(parent_node_item.name, child_node_item.name, parent_node_item.center_pos(),
                                             child_node_item.center_pos(), relationship)

        # Add RelationshipItem to the parent and child NodeItems
        parent_node_item.add_relationship(relationship_item.label, relationship_item)
        child_node_item.add_relationship(relationship_item.label, relationship_item)

        # Add to the scene and relationship dictionary
        self.graph_editor_scene.addItem(relationship_item)
        self.relationship_dictionary[relationship.label] = relationship_item
        self.selected_vector_item_group.add_to_list(relationship_item)

    def remove_vector(self, key):
        self.vector_dictionary.pop(key)

    def remove_node(self, key):
        self.node_dictionary.pop(key)

    def remove_relationship(self, key):
        self.relationship_dictionary.pop(key)


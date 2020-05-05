from typing import Dict
from src.gui.graph.graph_editor_view import GraphEditorView
from src.gui.graph.graph_editor_scene import GraphEditorScene
from src.gui.graph.node_item import NodeItem
from src.gui.graph.relationship_item import RelationshipItem
from src.gui.graph.vector_item_group import VectorItemGroup
from src.model.vector import Vector
from src.model.node import Node
from src.model.relationship import Relationship


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
        self.scene_width = 10000
        self.scene_height = 10000

        self.graph_editor_scene = GraphEditorScene(self.scene_width, self.scene_height)
        self.graph_editor_view = GraphEditorView(self.graph_editor_scene, parent)
        # self.test()

    # def test(self):
    #     vector = Vector(vector_name="V1")
    #     self.add_vector(vector)
    #     node1 = Node(name="Test_Node1")
    #     node2 = Node(name="Test_Node2")
    #     self.add_node(node1)
    #     self.add_node(node2)
    #
    #     relationship = Relationship(node1.id, node2.id, "Test_Relationship1")
    #     self.add_relationship(relationship)
    #     self.remove_vector(vector)

    '''
        Handles what VectorItemGroup should be displayed in the View and sets the working vector for this object
        :param vector : Vector
            The given vector for the realted VectorItemGroup 
    '''

    def display_vector(self, vector: Vector):
        # First check if the vector is in the dictionary if not then create it
        if vector.id in self.vector_dictionary:
            self.selected_vector_item_group = self.vector_dictionary[vector.id]
        else:
            self.add_vector(vector)
            self.selected_vector_item_group = self.vector_dictionary[vector.id]

        self.toggle_visibility(vector)

    '''
        Toggles the visibility of the current VectorItemGroup to the related Vector
        :param vector : Vector
            The vector to be made visible through VectorItemGroup
    '''

    def toggle_visibility(self, vector: Vector):
        # Toggle the visibility of the selected VectorItemGroup and hide the others
        for vector_group in self.vector_dictionary.values():
            if vector.id == vector_group.id:
                vector_group.unlock_display()
                vector_group.setVisible(False)
            else:
                vector_group.lock_hide()
                vector_group.hide()

    '''
        Creates a new VectorItem and toggles the view to it so that we can edit it
        :param vector:
            the vector used to create the VectorItemGroup
    '''

    def add_vector(self, vector: Vector):
        new_vector = VectorItemGroup(vector)
        self.graph_editor_scene.addItem(new_vector)
        self.vector_dictionary[vector.id] = new_vector
        self.selected_vector_item_group = new_vector
        self.toggle_visibility(vector)

    '''
        Used Node to create a NodeItem to be added to the GraphEditorScene
        :param node : Node
            The node used to create a new NodeItem
    '''

    def add_node(self, node: Node):
        polygon = self.graph_editor_view.mapFromScene(self.graph_editor_scene.sceneRect())
        point = polygon.boundingRect().center()
        node_item = NodeItem(point.x(), point.y(), node)
        self.graph_editor_scene.addItem(node_item)
        self.node_dictionary[node.id] = node_item
        self.selected_vector_item_group.add_to_list(node_item.id, node_item)

    '''
          Used Relationship to create a RelationshipItem to be added to the GraphEditorScene
          :param relationship : Relationship
              The Relationship used to create a new RelationshipItem
    '''

    def add_relationship(self, relationship: Relationship):
        # Find the nodes for this relationship in the node dictionary
        parent_node_item = self.node_dictionary[relationship.parent]
        child_node_item = self.node_dictionary[relationship.child]

        # Create the relationship
        relationship_item = RelationshipItem(parent_node_item.id, child_node_item.id, parent_node_item.center_pos(),
                                             child_node_item.center_pos(), relationship)
        # Add RelationshipItem to the parent and child NodeItems
        parent_node_item.add_relationship(relationship_item.id, relationship_item)
        child_node_item.add_relationship(relationship_item.id, relationship_item)

        # Add to the scene and relationship dictionary
        self.graph_editor_scene.addItem(relationship_item)
        self.relationship_dictionary[relationship.id] = relationship_item
        self.selected_vector_item_group.add_to_list(relationship_item.id, relationship_item)

    '''
        Removes the VectorItemGroup related to the given Vector and all the QGraphicsItems inside of it
        :param vector : Vector
            The Vector related to the VectorItemGroup to be deleted
    '''

    def remove_vector(self, vector: Vector):
        vector_item = self.vector_dictionary.pop(vector.id)
        for item in vector_item.item_dictionary.values():
            self.graph_editor_scene.removeItem(item)
        self.graph_editor_scene.removeItem(vector_item)

    '''
        Removes the NodeItem related to the given Node and all the RelationshipItems within it
        :param node : Node
            The Node related to the NodeItem to be deleted
                
    '''

    def remove_node(self, node: Node):
        node_item = self.selected_vector_item_group.item_dictionary.pop(node.id)
        for relationship in node_item.relationships.values():
            self.graph_editor_scene.removeItem(relationship)
        self.graph_editor_scene.removeItem(node_item)

    '''
        Removes the RelationshipItem related to the given Relationship
        :param relationship : Relationship
            The Relationship related to the RelationshipItem to be deleted
            
    '''

    def remove_relationship(self, relationship: Relationship):
        relationship_item = self.selected_vector_item_group.item_dictionary.pop(relationship.id)
        self.graph_editor_scene.removeItem(relationship_item)

"""vector.py: A vector dictionary and vector object."""

__author__ = "Team Keikaku"

__version__ = "0.7"

from PyQt5.QtCore import QObject, pyqtSignal
from src.model.node import Node
from src.model.relationship import Relationship


class VectorDictionary(QObject):
    """A dictionary of vectors and associated UUIDs.

    Attributes
    ----------
    vectors : dict
        A dictionary of vectors and their associated UUIDs.
    added_vector : pyqtSignal
        A pyQT signal emitted when a vector is added.
    removed_vector : pyqtSignal
        A pyQT signal emitted when a vector is removed.
    edited_vector : pyqtSignal
        A pyQT signal emitted when a vector is edited.
    """

    vectors: dict
    added_vector = pyqtSignal()
    removed_vector = pyqtSignal()
    edited_vector = pyqtSignal()

    def __init__(self):
        """Initializes the vector dictionary and pyQT signals."""

        QObject.__init__(self)
        self.vectors = {}

    def items(self):
        """Retrieves all items in the vector dictionary.

        :return Vector
            Vector associated with the given UUID.
        """

        return self.vectors.items()

    def get(self, vector_id: str):
        """Retrieves a vector given it's UUID.

        :param vector_id : str
            UUID of the vector.
        :return Vector
            Vector associated with the given UUID.
        """

        return self.vectors.get(vector_id)

    def empty(self) -> bool:
        """Determines of the dictionary is empty.

        :return
            True if vector dictionary is empty; false otherwise.
        """

        return not bool(self.vectors)

    def add_vector(self, vector_id: str, vector_name: str):
        """Adds a new vector to the vector dictionary. Emits added_vector.

        :param vector_id : str
            UUID of the vector.
        :param vector_name : str
            Name of the vector.
        """

        self.vectors[vector_id] = Vector(vector_name)
        self.added_vector.emit()

    def delete_vector(self, vector_id: str):
        """Removes a vector from the vector dictionary. Emits removed_vector.

        :param vector_id : str
            UUID of the vector.
        """

        self.vectors.pop(vector_id)
        self.removed_vector.emit()

    def edit_vector(self):
        """Emits edited_vector that a vector in the dictionary was edited."""

        self.edited_vector.emit()


class Vector:
    """A class representing an attack vector.

    A vector consisting of a name and description along with dictionaries
    of nodes and relations.

    Attributes
    ----------
    name : str
        Name of the vector.
    description : str
        Description of the vector.
    nodes : dict
        A dictionary of nodes.
    relationships : dict
        A dictionary of relationships.
    """

    name: str
    description: str
    nodes: dict
    relationships: dict

    def __init__(self, vector_name: str = 'New Vector', vector_desc: str = ''):
        """
        :param vector_name : str, optional (default is 'New Vector')
            Name of the vector.
        :param vector_desc : str, optional
            Description of the vector (default is '').
        """

        self.name = vector_name
        self.description = vector_desc
        self.nodes = {}
        self.relationships = {}

    def edit_name(self, vector_name: str):
        """Updates the name of a vector.

        :param vector_name : str
            Name of the vector.
        """

        self.name = vector_name

    def edit_desc(self, vector_desc: str):
        """Updates the description of a vector.

        :param vector_desc : str
            Description of the vector.
        """

        self.description = vector_desc

    def add_node(self, node_id: str):
        """Adds a new node to the node dictionary.

        :param node_id: str
            UUID of the node.
        """

        self.nodes[node_id] = Node()

    def delete_node(self, node_id: str):
        """Removes a node from the node dictionary.

        :param node_id: str
            UUID of the node.
        """

        self.nodes.pop(node_id)

    def node_items(self):
        """Retrieves all items in the node dictionary.

        :return Node
            Node associated with the given UUID.
        """

        return self.nodes.items()

    def node_get(self, node_id: str):
        """Retrieves a node given it's UUID.

        :param node_id : str
            UUID of the node.
        :return Node
            Node associated with the given UUID.
        """

        return self.nodes.get(node_id)

    def add_relationship(self, relationship_id: str):
        """Adds a new relationship to the relationship dictionary.

        :param relationship_id: str
            UUID of the relationship.
        """

        self.relationships[relationship_id] = Relationship()

    def delete_relationship(self, relationship_id: str):
        """Removes a relationship from the relationship dictionary.

        :param relationship_id: str
            UUID of the relationship.
        """

        self.relationships.pop(relationship_id)

    def relationship_items(self):
        """Retrieves all items in the relationship dictionary.

        :return relationship
            Relationship associated with the given UUID.
        """

        return self.relationships.items()

    def relationship_get(self, relationship_id: str):
        """Retrieves a vector given it's UUID.

        :param relationship_id : str
            UUID of the relationship.
        :return Relationship
            Relationship associated with the given UUID.
        """

        return self.relationships.get(relationship_id)


class ActiveVector:
    """An active vector which displays across the system.

    Attributes
    ----------
    vector : Vector
        The active vector.
    vector_id : str
        The UUID of the active vector.
    """

    vector: Vector
    vector_id: str

    def __init__(self, vector: Vector = None, vector_id: str = ''):
        """
        :param vector (default is None)
            The vector to set active.
        :param vector_id (default is '')
            The UUID of the vector to set active.
        """

        self.set(vector, vector_id)

    def set(self, vector: Vector = None, vector_id: str = ''):
        """Sets the active vector and its UUID.

        :param vector (default is None)
            The vector to set active.
        :param vector_id (default is '')
            The UUID of the vector to set active.
        """

        self.vector = vector
        self.vector_id = vector_id

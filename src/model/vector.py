"""vector.py: A collection of information representing an
a collection of events during an adversarial assessment."""

__author__ = "Team Keikaku"

__version__ = "0.7"

from src.model.id_dictionary import IDDict
from src.model.node import Node
from src.model.relationship import Relationship


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
    nodes: IDDict
    relationships: IDDict

    def __init__(self, vector_name: str = 'New Vector', vector_desc: str = ''):
        """
        :param vector_name : str, optional (default is 'New Vector')
            Name of the vector.
        :param vector_desc : str, optional
            Description of the vector (default is '').
        """

        self.name = vector_name
        self.description = vector_desc
        self.nodes = IDDict()
        self.relationships = IDDict()

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
            UID of the node.
        """

        self.nodes.add(node_id, Node())

    def delete_node(self, node_id: str):
        """Removes a node from the node dictionary.

        :param node_id: str
            UID of the node.
        """

        self.nodes.delete(node_id)

    def node_items(self):
        """Retrieves all items in the node dictionary.

        :return Node
            Node associated with the given UID.
        """

        return self.nodes.items()

    def node_get(self, node_id: str):
        """Retrieves a node given it's UID.

        :param node_id : str
            UID of the node.
        :return Node
            Node associated with the given UID.
        """

        return self.nodes.get(node_id)

    def add_relationship(self, relationship_id: str):
        """Adds a new relationship to the relationship dictionary.

        :param relationship_id: str
            UID of the relationship.
        """

        self.relationships.add(relationship_id, Relationship())

    def delete_relationship(self, relationship_id: str):
        """Removes a relationship from the relationship dictionary.

        :param relationship_id: str
            UID of the relationship.
        """

        self.relationships.delete(relationship_id)

    def relationship_items(self):
        """Retrieves all items in the relationship dictionary.

        :return relationship
            Relationship associated with the given UID.
        """

        return self.relationships.items()

    def relationship_get(self, relationship_id: str):
        """Retrieves a vector given it's UID.

        :param relationship_id : str
            UID of the relationship.
        :return Relationship
            Relationship associated with the given UID.
        """

        return self.relationships.get(relationship_id)


class ActiveVector:
    """An active vector which displays across the system.

    Attributes
    ----------
    vector : Vector
        The active vector.
    vector_id : str
        The UID of the active vector.
    """

    vector: Vector
    vector_id: str

    def __init__(self, vector: Vector = None, vector_id: str = ''):
        """
        :param vector (default is None)
            The vector to set active.
        :param vector_id (default is '')
            The UID of the vector to set active.
        """

        self.set(vector, vector_id)

    def set(self, vector: Vector = None, vector_id: str = ''):
        """Sets the active vector and its UID.

        :param vector (default is None)
            The vector to set active.
        :param vector_id (default is '')
            The UID of the vector to set active.
        """

        self.vector = vector
        self.vector_id = vector_id

"""vector.py: A collection of information representing an
a collection of events during an adversarial assessment.

    Classes
    ----------
    Vector
        A collection of information representing an attack vector.
    ActiveVector
        An active vector which the system is focused on.
"""

__author__ = "Team Keikaku"

__version__ = "0.7"

from src.model.id_dictionary import IDDict
from src.model.node import Node
from src.model.relationship import Relationship


class Vector:
    """A collection of information representing an attack vector.

    A vector consisting of a name and description along with dictionaries
    of nodes and relations.

    Attributes
    ----------
    name: str
        Name of the vector.
    description: str
        Description of the vector.
    property_visibility: int
        Bit set representing all the property visibilities.
    nodes: dict
        A dictionary of nodes.
    relationships: dict
        A dictionary of relationships.
    """

    name: str
    description: str
    property_visibility: int
    nodes: IDDict
    relationships: IDDict

    def __init__(self, vector_name: str = 'New Vector', vector_desc: str = '', property_visibility: int = 0,
                 nodes: dict = {}, relationships: dict = {}):
        """
        :param vector_name: str, optional (default is 'New Vector')
            Name of the vector.
        :param vector_desc: str, optional (default is '')
            Description of the vector.
        :param property_visibility: int, optional (default is 0)
            Vector property visibility flags.
        :param nodes: dict, optional (default is {})
            A dictionary of nodes.
        :param relationships: dict, optional (default is {})
            A dictionary of relationships.
        """

        self.name = vector_name
        self.description = vector_desc
        self.property_visibility = property_visibility
        self.nodes = IDDict(dictionary=nodes)
        self.relationships = IDDict(dictionary=relationships)

    def edit_name(self, vector_name: str):
        """Updates the name of a vector.

        :param vector_name: str
            Name of the vector.
        """

        self.name = vector_name

    def edit_desc(self, vector_desc: str):
        """Updates the description of a vector.

        :param vector_desc: str
            Description of the vector.
        """

        self.description = vector_desc

    def add_node(self) -> str:
        """Adds a new node to the node dictionary.

        :return str
            A UID associated with the node added.
        """

        return self.nodes.add(Node())

    def delete_node(self, node_id: str):
        """Removes a node from the node dictionary.

        :param node_id: str
            UID of the node.
        """

        self.nodes.delete(node_id)

    def node_items(self):
        """Retrieves all items in the node dictionary.

        :return dict_items
            A list of node_id, Node tuples.
        """

        return self.nodes.items()

    def node_get(self, node_id: str) -> Node:
        """Retrieves a node given it's UID.

        :param node_id: str
            UID of the node.
        :return Node
            Node associated with the given UID.
        """

        return self.nodes.get(node_id)

    def add_relationship(self) -> str:
        """Adds a new relationship to the relationship dictionary.

        :return str
            A UID associated with the relationship added.
        """

        return self.relationships.add(Relationship())

    def delete_relationship(self, relationship_id: str):
        """Removes a relationship from the relationship dictionary.

        :param relationship_id: str
            UID of the relationship.
        """

        self.relationships.delete(relationship_id)

    def relationship_items(self):
        """Retrieves all items in the relationship dictionary.

        :return dict_items
            A list of relationship_id, Relationship tuples.
        """

        return self.relationships.items()

    def relationship_get(self, relationship_id: str) -> Relationship:
        """Retrieves a vector given it's UID.

        :param relationship_id: str
            UID of the relationship.
        :return Relationship
            Relationship associated with the given UID.
        """

        return self.relationships.get(relationship_id)

    def toggle_node_id_visibility(self):
        """Toggles the node_id_visibility."""

        self.property_visibility ^= 1

    def get_node_id_visibility(self) -> bool:
        """Determines if node_id_visibility is set.

        :return bool
            True if node_id_visibility is set, false otherwise.
        """

        return bool(self.property_visibility & 1)

    def toggle_node_name_visibility(self):
        """Toggles the node_name_visibility."""

        self.property_visibility ^= 2

    def get_node_name_visibility(self) -> bool:
        """Determines if node_name_visibility is set.

        :return bool
            True if node_name_visibility is set, false otherwise.
        """

        return bool(self.property_visibility & 2)

    def toggle_node_time_visibility(self):
        """Toggles the node_time_visibility."""

        self.property_visibility ^= 4

    def get_node_time_visibility(self) -> bool:
        """Determines if node_time_visibility is set.

        :return bool
            True if node_time_visibility is set, false otherwise.
        """

        return bool(self.property_visibility & 4)

    def toggle_node_desc_visibility(self):
        """Toggles the node_desc_visibility."""

        self.property_visibility ^= 8

    def get_node_desc_visibility(self) -> bool:
        """Determines if node_desc_visibility is set.

        :return bool
            True if node_desc_visibility is set, false otherwise.
        """

        return bool(self.property_visibility & 8)

    def toggle_log_entry_visibility(self):
        """Toggles the log_entry_visibility."""

        self.property_visibility ^= 16

    def get_log_entry_visibility(self) -> bool:
        """Determines if log_entry_visibility is set.

        :return bool
            True if log_entry_visibility is set, false otherwise.
        """

        return bool(self.property_visibility & 16)

    def toggle_log_creator_visibility(self):
        """Toggles the log_creator_visibility."""

        self.property_visibility ^= 32

    def get_log_creator_visibility(self) -> bool:
        """Determines if log_creator_visibility is set.

        :return bool
            True if log_creator_visibility is set, false otherwise.
        """

        return bool(self.property_visibility & 32)

    def toggle_event_type_visibility(self):
        """Toggles the event_type_visibility."""

        self.property_visibility ^= 64

    def get_event_type_visibility(self) -> bool:
        """Determines if event_type_visibility is set.

        :return bool
            True if event_type_visibility is set, false otherwise.
        """

        return bool(self.property_visibility & 64)

    def toggle_icon_type_visibility(self):
        """Toggles the icon_type_visibility."""

        self.property_visibility ^= 128

    def get_icon_type_visibility(self) -> bool:
        """Determines if icon_type_visibility is set.

        :return bool
            True if icon_type_visibility is set, false otherwise.
        """

        return bool(self.property_visibility & 128)

    def toggle_source_visibility(self):
        """Toggles the source_visibility."""

        self.property_visibility ^= 256

    def get_source_visibility(self) -> bool:
        """Determines if source_visibility is set.

        :return bool
            True if source_visibility is set, false otherwise.
        """

        return bool(self.property_visibility & 256)


class ActiveVector:
    """An active vector which the system is focused on.

    Attributes
    ----------
    vector: Vector
        The active vector.
    vector_id: str
        The UID of the active vector.
    """

    vector: Vector
    vector_id: str

    def __init__(self, vector: Vector = None, vector_id: str = ''):
        """
        :param vector: Vector, optional (default is None)
            The vector to set active.
        :param vector_id: str, optional (default is '')
            The UID of the vector to set active.
        """

        self.set(vector, vector_id)

    def set(self, vector: Vector = None, vector_id: str = ''):
        """Sets the active vector and its UID.

        :param vector: Vector (default is None)
            The vector to set active.
        :param vector_id: str (default is '')
            The UID of the vector to set active.
        """

        self.vector = vector
        self.vector_id = vector_id

    def is_empty(self) -> bool:
        """Determines if the active vector is empty.

        :return bool
            True if the active vector is empty, false otherwise.
        """
        return not bool(self.vector)

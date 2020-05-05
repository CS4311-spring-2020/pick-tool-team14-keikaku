"""relationship.py: A collection of information representing an
link between a parent and child event in a vector.
"""

__author__ = "Team Keikaku"
__version__ = "1.0"


class Relationship:
    """A collection of information representing a link between a parent and child node.

    Attributes
    ----------
    parent: str
        UUID of the parent node.
    child: str
        UUID of the child node.
    label: str
        Label of the relationship.
    """

    parent: str
    child: str
    label: str

    def __init__(self, parent: str = '', child: str = '', label: str = ''):
        """
        :param parent: str, optional  (default is '')
            UUID of the parent node.
        :param child: str, optional  (default is '')
            UUID of the child node.
        :param label: str, optional  (default is '')
            Label of the relationship.
        """

        self.parent = parent
        self.child = child
        self.label = label

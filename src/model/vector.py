"""vector.py: A dictionary of vectors.

    Attributes
    ----------
    vectors : dict
        A dictionary of vectors.
"""

__author__ = "Team Keikaku"

__version__ = "0.5"

vectors: dict = {}


def add_vector(vector_id: str, vector_name: str):
    """Adds a new vector to the vector dictionary.

    Parameters
    ----------
    vector_id : str
        UUID of the vector.
    vector_name : str
        Name of the vector.
    """

    # print('Adding vector : ' + str(vector_id))
    vectors[vector_id] = Vector(vector_name)


def delete_vector(vector_id: str):
    """Removes a vector from the vector dictionary.

    Parameters
    ----------
    vector_id : str
        UUID of the vector.
    """

    # print('Removing vector : ' + str(vector_id))
    vectors.pop(vector_id)


def edit_vector_name(vector_id: str, vector_name: str):
    """Updates the name of a vector.

    Parameters
    ----------
    vector_id : str
        UUID of the vector.
    vector_name : str
        Name of the vector.
    """

    vectors[vector_id].name = vector_name
    # print('Changed vector name to: ' + str(vectors[vector_id].name))


def edit_vector_desc(vector_id: str, vector_desc: str):
    """Updates the description of a vector.

    Parameters
    ----------
    vector_id : str
        UUID of the vector.
    vector_desc : str
        Description of the vector.
    """

    vectors[vector_id].description = vector_desc
    print('Changed vector description to: ' + str(vectors[vector_id].description))


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
    relations : dict
        A dictionary of relations.
    """

    name: str
    description: str
    nodes: dict
    relations: dict

    def __init__(self, vector_name: str = 'New Vector', vector_desc: str = ''):
        """
        Parameters
        ----------
        vector_name : str, optional (default is 'New Vector')
            Name of the vector.
        vector_desc : str, optional
            Description of the vector (default is '').
        """

        self.name = vector_name
        self.description = vector_desc

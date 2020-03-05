"""file_util.py: A set of subroutines related to file processing.

    Methods
    -------
    save_object(obj: Any, filename: str)
        Saves an object in a file.
    read_file(filename: str) -> Any
        Reads an object from a file.
    check_file(filename: str) -> bool
        Checks if filename exists.
"""

__author__ = "Team Keikaku"

__version__ = "0.5"

import os
import pickle
from typing import Any

from definitions import CACHE_PATH


def save_object(obj: Any, filename: str):
    """Saves an object in a file.

    :param obj: Any
        Object to save.
    :param filename: str
        Name of the file to save obj to.
    """

    if not os.path.isdir(CACHE_PATH):
        os.mkdir(CACHE_PATH)
    with open(os.path.join(CACHE_PATH, filename), 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def read_file(filename: str) -> Any:
    """Reads an object from a file.

    :param filename: str
        Name of the file to read from.
    :return Any
        Object read from file.
    """

    with open(os.path.join(CACHE_PATH, filename), 'rb') as data:
        return pickle.load(data)


def check_file(filename: str) -> bool:
    """Checks if filename exists.

    :return
        True is filename exists, false otherwise.
    """

    return os.path.exists(os.path.join(CACHE_PATH, filename))

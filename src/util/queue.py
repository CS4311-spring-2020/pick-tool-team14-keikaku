"""queue.py: A collection of information representing a log entry.
"""

__author__ = "Team Keikaku"
__version__ = "1.0"

from typing import Any


class Queue:
    """A simple queue implementation.

        Attributes
        ----------
        items: List[Any]
            Array to be used as a queue.
    """

    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        """Returns true if the queue is empty, false otherwise.

        :return: bool
            true if the queue is empty, false otherwise.
        """

        return not self.items

    def enqueue(self, item: Any):
        """Inserts an item into the front of the queue.

        :param item: Any
            The item to put into the queue.
        """

        self.items.insert(0, item)

    def dequeue(self) -> Any:
        """Removes and retrieves the last item from the queue.

        :return: Any
            The last item from the queue.
        """

        return self.items.pop()

    def size(self) -> int:
        """Returns the size of the queue.

        :return: int
            Size of the queue.
        """

        return len(self.items)

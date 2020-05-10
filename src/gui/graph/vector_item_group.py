from typing import Dict

from PyQt5.Qt import QGraphicsItemGroup, QGraphicsItem, QRectF

from src.model.vector import Vector


class VectorItemGroup(QGraphicsItemGroup):
    """
        The VectorItemGroup provides a container that treats a group of items as a single item and draws their bounding
        box.

        Attributes
        ----------
        vector_id : str
            unique identifier for this class
        bound_box : QRectF
            Bound box used to draw tha bounding box of all the items inside this class
    """
    uid: str
    bound_box: QRectF
    vector: Vector
    item_dictionary: Dict[str, QGraphicsItem] = {}

    def __init__(self, vector: Vector):
        super().__init__()
        self.uid = vector.uid
        self.vector = vector

    def add_to_list(self, uid: str, item: QGraphicsItem):
        self.item_dictionary[uid] = item

    def remove_from_list(self, uid: str):
        self.item_dictionary.pop(uid)

    def lock_hide(self):
        for item in self.item_dictionary.values():
            self.addToGroup(item)

    def unlock_display(self):
        for item in self.item_dictionary.values():
            self.removeFromGroup(item)

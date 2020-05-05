from typing import List
from PyQt5.Qt import QGraphicsItemGroup, QGraphicsItem, QRectF, QPen, QGraphicsRectItem, Qt
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
    name: str
    bound_box: QRectF
    vector : Vector
    item_list : List[QGraphicsItem] = []

    def __init__(self, vector : Vector):
        super().__init__()
        self.name = vector.name
        self.vector = vector

    def add_to_list(self, item : QGraphicsItem):
        self.item_list.append(item)

    def remove_from_list(self, item : QGraphicsItem):
        self.item_list.remove(item)

    def lock_and_hide(self):
        for item in self.item_list:
            self.addToGroup(item)
        self.setVisible(False)

    def unlock_displac(self):
        for item in self.item_list:
            item.setVisible(True)
            self.removeFromGroup(item)

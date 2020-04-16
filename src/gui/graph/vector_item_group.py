from PyQt5.Qt import QGraphicsItemGroup
from PyQt5.Qt import QRectF
from PyQt5.Qt import QPainter
from PyQt5.Qt import QPen
from PyQt5.Qt import QBrush
from PyQt5.Qt import QStyleOptionGraphicsItem
from PyQt5.Qt import Qt
from PyQt5.Qt import QGraphicsRectItem

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
    vector_id : str
    bound_box : QRectF

    def __init__(self):
        super().__init__()


    '''
        Draws bounding box that contains all the items inside it.
    '''
    def get_bound_box_item(self):
        self.bound_box = self.boundingRect()
        bound_box_item = QGraphicsRectItem(self.bound_box.x(), self.bound_box.y(), self.bound_box.height(), self.bound_box.width())
        bound_box_item.setPen(QPen(Qt.green, 6))
        return bound_box_item
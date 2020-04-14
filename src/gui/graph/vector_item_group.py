from PyQt5.Qt import QGraphicsItemGroup
from PyQt5.Qt import QRectF
from PyQt5.Qt import QPainter
from PyQt5.Qt import QPen
from PyQt5.Qt import QBrush
from PyQt5.Qt import QStyleOptionGraphicsItem
from PyQt5.Qt import Qt
from PyQt5.Qt import QGraphicsRectItem

class VectorItemGroup(QGraphicsItemGroup):

    vector_id : str
    bound_box : QRectF

    def __init__(self):
        super().__init__()

    def get_bound_box_item(self):
        self.bound_box = self.boundingRect()
        bound_box_item = QGraphicsRectItem(self.bound_box.x(), self.bound_box.y(), self.bound_box.height(), self.bound_box.width())
        bound_box_item.setPen(QPen(Qt.green, 6))
        return bound_box_item
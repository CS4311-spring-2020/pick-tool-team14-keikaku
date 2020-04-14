from PyQt5.Qt import QGraphicsLineItem
from PyQt5.Qt import QLine
from PyQt5.Qt import QPoint
from PyQt5.Qt import QPen
from PyQt5.Qt import Qt

class RelationshipItem(QGraphicsLineItem):
    parent_node : str
    child_node :str

    def __init__(self, parent_node, child_node, parent_point : QPoint, child_point : QPoint, parent=None):
        super().__init__(parent_point.x(), parent_point.y(), child_point.x(), child_point.y())
        self.parent_node = parent_node
        self.child_node = child_node
        self.setPen(QPen(Qt.yellow, 6))





from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.Qt import QGraphicsLineItem


class NodeItem(QGraphicsItem):
    width: float = 100.0
    height: float = 100.0
    relationships = {}

    def __init__(self,  pos_x : float, post_y : float, name : str, type : str, parent=None):
        super().__init__(parent)
        self.pos_x = pos_x
        self.pos_y = post_y
        self.name = name
        self.type = type

        self.init_ui()

    def center_pos(self):
        return self.boundingRect().center()

    def add_relationship(self, key : str, relationship):
        self.relationships[key] = relationship

    def add_line(self, line : QGraphicsLineItem):
        self.line = line

    def init_ui(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setAcceptHoverEvents(True)

    def boundingRect(self) -> QRectF:
        """Defining Qt' bounding rectangle"""
        return QRectF(self.pos_x, self.pos_y, self.width, self.height).normalized()

    def paint(self, painter: QPainter, style: QStyleOptionGraphicsItem, widget=None):
        node_outline = QPainterPath()
        node_outline.addEllipse(self.pos_x, self.pos_y, self.width, self.height)
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.red))
        painter.drawPath(node_outline.simplified())
        # node_outline.setFlag(QGraphicsItem.ItemIsMovable)

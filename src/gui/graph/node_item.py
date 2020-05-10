from typing import Dict
from PyQt5.Qt import Qt, QGraphicsItem, QPainter, QPainterPath, QStyleOptionGraphicsItem, QPen, QBrush, QPoint, \
    QRectF, QGraphicsSimpleTextItem
from PyQt5.QtWidgets import QGraphicsSceneMouseEvent
from src.model.node import Node
from src.gui.graph.relationship_item import RelationshipItem


class NodeItem(QGraphicsItem):
    '''
        NodeItem is a graphical item class that draws nodes and hold node information and relationships

        Attributes
        ----------
        width : float
            width of node
        height : float
            height of node
        relationship : dict
            RelationshipItem that links one node to another
    '''
    width: float = 100.0
    height: float = 100.0
    relationships: Dict[str, RelationshipItem] = {}
    node: Node
    uid: str
    text: QGraphicsSimpleTextItem

    def __init__(self, x: float, y: float, node: Node, parent=None):
        super().__init__(parent)
        self.pos_x = x
        self.pos_y = y
        self.uid = node.uid
        self.node = node
        self.set_text_item(node.name)
        self.init_ui()

    def init_ui(self):
        self.setZValue(1)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsScenePositionChanges)
        self.setAcceptHoverEvents(True)

    def set_text_item(self, text: str):
        """
        This method sets the QGraphicsSimpleTextItem for this class
        :param text : str
            The text to set up for the text box of this node
        """
        self.text = QGraphicsSimpleTextItem(text, self)
        self.text.setBrush(QBrush(Qt.white))
        self.text.setX(self.pos().x() - 20)
        self.text.setY(self.pos().y() - 20)

    def change_text(self, text):
        self.text.setText(text)

    def center_pos(self):
        """
        Grabs the initial boundingRect of this node and translates the current position of the mid point
        """
        # grab the bounding rectangle for this class on it's coordinate position
        center, current = self.boundingRect().center(), self.pos()
        return QPoint(current.x() + center.x(), current.y() + center.y())

    def add_relationship(self, key: str, relationship: RelationshipItem):
        """
        Add a relationship to the node
        :param key: str
            unique identifier for the relationship
        :param relationship: RelationshipItem
            graphics object that connects to this node
        """
        print(type(relationship))
        self.relationships[key] = relationship

    def boundingRect(self) -> QRectF:
        """
        Defines QRect bounding rectangle which contains this node
        :return: QRectF
            bounding rectangle for this node
        """
        return QRectF(self.pos_x, self.pos_y, self.width, self.height).normalized()

    def paint(self, painter: QPainter, style: QStyleOptionGraphicsItem, widget=None):
        """
        This function which is usually called by QGraphicsView, paints the contents of an item in local coordinates.

        :param painter: QPainter
            Class that handles painter the item on the scene
        :param style: QStyleOptionGraphicsItem
            Style options used on this item, usually defaulted
        :param widget: QWidget
            Widget to paint this item on
        """
        node_outline = QPainterPath()
        node_outline.addEllipse(self.pos_x, self.pos_y, self.width, self.height)
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.red))
        painter.drawPath(node_outline.simplified())

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        """
        Overrides the inherited mouse event so that it can update the coordinates of the connected relationships

        :param event: QGraphicsSceneMouseEvent
            mouse event for when this node is click and moved
        """
        super().mouseMoveEvent(event)
        for rl in self.relationships.values():
            rl.dragLine(self.uid, self.center_pos())

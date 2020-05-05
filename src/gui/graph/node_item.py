from typing import Dict
from PyQt5.Qt import Qt, QGraphicsItem, QPainter, QPainterPath, QStyleOptionGraphicsItem, QPen, QBrush, QPoint, QRectF
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
    relationships : Dict[str, RelationshipItem] = {}
    node : Node
    id = str

    def __init__(self, x: float, y: float, node: Node, parent=None):
        super().__init__(parent)
        self.pos_x = x
        self.pos_y = y
        self.id = node.id
        self.node = node

        self.init_ui()

    def init_ui(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsScenePositionChanges)
        self.setAcceptHoverEvents(True)

    '''
        Grabs the initial boundingRect of this node and translates the current position of the mid point 
    '''

    def center_pos(self):
        # grab the bounding rectangle for this class on it's coordinate position
        center, current = self.boundingRect().center(), self.pos()
        return QPoint(current.x() + center.x(), current.y() + center.y())

    '''
        Add a relationship to the node
        
        Parameters
        ----------
        key : str
            unique identifier for the relationship
        relationship : RelationshipItem
            graphics object that connects to this node       
    '''

    def add_relationship(self, key: str, relationship : RelationshipItem):
        print(type(relationship))
        self.relationships[key] = relationship

    '''
        Defines QRect bounding rectangle which contains this node
        
        Return
        ------
        QRectF
            bounding rectangle for this node
    '''

    def boundingRect(self) -> QRectF:
        return QRectF(self.pos_x, self.pos_y, self.width, self.height).normalized()

    '''
        This function which is usually called by QGraphicsView, paints the contents of an item in local coordinates.
        
        Parameters
        ----------    
        painter: QPainter
            Class that handles painter the item on the scene
        style: QStyleOptionGraphicsItem
            Style options used on this item, usually defaulted
        widget : QWidget
            Widget to paint this item on
    '''

    def paint(self, painter: QPainter, style: QStyleOptionGraphicsItem, widget=None):
        node_outline = QPainterPath()
        node_outline.addEllipse(self.pos_x, self.pos_y, self.width, self.height)
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.red))
        painter.drawPath(node_outline.simplified())


    '''
        Overrides the inherited mouse event so that it can update the coordinates of the connected relationships
        
        :param event : QGraphicsSceneMouseEvent
            mouse event for when this node is click and moved
    '''
    def mouseMoveEvent(self, event :QGraphicsSceneMouseEvent):
        super().mouseMoveEvent(event)
        for rl in self.relationships.values():
            rl.dragLine(self.id, self.center_pos())



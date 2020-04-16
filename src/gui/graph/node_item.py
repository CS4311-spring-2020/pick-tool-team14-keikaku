from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.Qt import QGraphicsLineItem


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
    relationships = {}

    def __init__(self, pos_x: float, post_y: float, name: str, type: str, parent=None):
        super().__init__(parent)
        self.pos_x = pos_x
        self.pos_y = post_y
        self.name = name
        self.type = type

        self.init_ui()

    def init_ui(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setAcceptHoverEvents(True)

    '''
        Returns the center position of a node
    '''

    def center_pos(self):
        return self.boundingRect().center()

    '''
        Add a relationship to the node
        
        Parameters
        ----------
        key : str
            unique identifier for the relationship
        relationship : RelationshipItem
            graphics object that connects to this node       
    '''

    def add_relationship(self, key: str, relationship):
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
        This funtion which is usually called by QGraphicsView, paints the contents of an item in local coordinates.
        
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

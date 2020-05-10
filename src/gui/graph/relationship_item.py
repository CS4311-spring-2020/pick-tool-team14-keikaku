from typing import Dict

from PyQt5.Qt import QGraphicsLineItem, QGraphicsItem, QPoint, QPen, Qt

from src.model.relationship import Relationship


class RelationshipItem(QGraphicsLineItem):
    '''
        RelationShipItem provides a line item that you can add to a GraphEditorScene by using QPoint

        Attributes
        ----------
        parent_node : str
            parent Node class
        child_node : str
            child node class
    '''
    parent_node: str
    child_node: str
    coordinates: Dict[str, QPoint] = {}
    relationship: Relationship
    uid: str

    def __init__(self, parent_node: str, child_node: str, parent_point: QPoint, child_point: QPoint,
                 relationship: Relationship, parent=None):
        super().__init__(parent_point.x(), parent_point.y(), child_point.x(), child_point.y(), parent)
        self.parent_node = parent_node
        self.child_node = child_node
        self.coordinates[parent_node] = parent_point
        self.coordinates[child_node] = child_point
        self.uid = relationship.uid
        self.setPen(QPen(Qt.yellow, 6))
        self.setZValue(-1)
        self.setFlag(QGraphicsItem.ItemSendsScenePositionChanges)
        self.setAcceptHoverEvents(True)

    def dragLine(self, node_id: str, node_point: QPoint):
        """
        Method used to drag this RelationsItem's line with the new node positions
        :param node_id: str
            unique identifier for the changing node
        :param node_point: QPoint
            represents the midpoint of the changing node
        """
        self.coordinates[node_id] = node_point
        parent_point = self.coordinates[self.parent_node]
        child_point = self.coordinates[self.child_node]
        self.setLine(parent_point.x(), parent_point.y(), child_point.x(), child_point.y())

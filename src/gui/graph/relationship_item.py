from PyQt5.Qt import QGraphicsLineItem
from PyQt5.Qt import QGraphicsItem
from PyQt5.Qt import QPoint
from PyQt5.Qt import QPen
from PyQt5.Qt import Qt


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
    coordinates = {}
    name : None

    def __init__(self, parent_node, child_node, parent_point: QPoint, child_point: QPoint, name : str, parent=None):
        super().__init__(parent_point.x(), parent_point.y(), child_point.x(), child_point.y(), parent)
        self.parent_node = parent_node
        self.child_node = child_node
        self.coordinates[parent_node] = parent_point
        self.coordinates[child_node] = child_point
        self.name = name
        self.setPen(QPen(Qt.yellow, 6))

        self.init_ui()

    def init_ui(self):
        self.setFlag(QGraphicsItem.ItemSendsScenePositionChanges)
        self.setAcceptHoverEvents(True)

    def dragLine(self, node_name, node_point):
        self.coordinates[node_name] = node_point
        parent_point = self.coordinates[self.parent_node]
        child_point = self.coordinates[self.child_node]
        self.setLine(parent_point.x(), parent_point.y(), child_point.x(), child_point.y())
        print(self.line())

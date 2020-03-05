from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.Qt import QPainter
from PyQt5.Qt import QPainterPath
from PyQt5.Qt import QStyleOptionGraphicsItem
from PyQt5.Qt import QPen
from PyQt5.Qt import QColor
from PyQt5.Qt import QRectF
from PyQt5.QtWidgets import QGraphicsTextItem


class NodeGraphics(QGraphicsItem):
    def __init__(self, node, description="Node Graphics", parent=None):
        super().__init__(parent)

        self._title_color = Qt.white
        self._description_font = QFont("Verdana", 10)

        self.init_description()
        self.init_ui()

        # Protected setter for description
        self.description = description

        self.width = 180
        self.height = 240
        self.edge_size = 10.0
        self._pen_default = QPen(QColor("#7F000000"))
        self._pen_selected = QPen(QColor("#FFFFA637"))

    def init_ui(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    def init_description(self):
        self.description_item = QGraphicsTextItem(self)
        self.description_item.setDefaultTextColor(self._title_color)
        self.description_item.setFont(self._description_font)

    @property
    def description(self): return self._description

    @description.setter
    def description(self, value):
        self._description = value
        self.description_item.setPlainText(self._description)

    def paint(self, painter: QPainter, style_options: QStyleOptionGraphicsItem, widget=None):
        # description

        # content

        # outline
        path_outline = QPainterPath()
        path_outline.addRoundedRect(0, 0, self.width, self.height, self.edge_size, self.edge_size)
        painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())

    def boundingRect(self):
        return QRectF(0, 0, 2 * self.edge_size + self.width, 2 * self.edge_size + self.height).normalized()

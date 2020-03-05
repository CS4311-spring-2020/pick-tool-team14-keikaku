from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.Qt import QPainter
from PyQt5.Qt import QPainterPath
from PyQt5.Qt import QStyleOptionGraphicsItem
from PyQt5.Qt import QPen
from PyQt5.Qt import QColor
from PyQt5.Qt import QBrush
from PyQt5.Qt import QRectF
from PyQt5.QtWidgets import QGraphicsTextItem


class NodeGraphics(QGraphicsItem):
    def __init__(self, node, name="Node Graphics", parent=None):
        super().__init__(parent)

        self._title_color = Qt.white
        self._name_font = QFont("Verdana", 10)

        self.width = 180
        self.height = 240
        self.edge_size = 10.0
        self.name_height = 24.0
        self._padding = 5.0
        self._pen_default = QPen(QColor("#7F000000"))
        self._pen_selected = QPen(QColor("#FFFFA637"))

        # Background for the name of the node
        self._brush_name = QBrush(QColor("#FF313131"))
        self._brush_background = QBrush(QColor("#E3121212"))

        self.init_name()
        # Protected setter for name
        self.name = name

        self.init_ui()

    def init_ui(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def init_name(self):
        self.name_item = QGraphicsTextItem(self)
        self.name_item.setDefaultTextColor(self._title_color)
        self.name_item.setFont(self._name_font)
        self.name_item.setPos(self._padding, 0)
        self.name_item.setFont(self._name_font)
        self.name_item.setTextWidth(self.width - 2 * self._padding)

    @property
    def name(self): return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.name_item.setPlainText(self._name)

    def paint(self, painter: QPainter, style_options: QStyleOptionGraphicsItem, widget=None):
        # name
        path_title = QPainterPath()
        path_title.setFillRule(Qt.WindingFill)
        path_title.addRoundedRect(0, 0, self.width, self.name_height, self.edge_size, self.edge_size)
        path_title.addRect(0, self.name_height - self.edge_size, self.edge_size, self.edge_size)
        path_title.addRect(self.width - self.edge_size, self.name_height - self.edge_size,
                           self.edge_size, self.edge_size)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_name)
        painter.drawPath(path_title.simplified())

        # content
        path_content = QPainterPath()
        path_content.setFillRule(Qt.WindingFill)
        path_content.addRoundedRect(0, self.name_height, self.width, self.height - self.name_height, self.edge_size,
                                    self.edge_size)
        path_content.addRect(0, self.name_height, self.edge_size, self.edge_size)
        path_content.addRect(self.width - self.edge_size, self.name_height, self.edge_size, self.edge_size)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_background)
        painter.drawPath(path_content.simplified())
        # outline
        path_outline = QPainterPath()
        path_outline.addRoundedRect(0, 0, self.width, self.height, self.edge_size, self.edge_size)
        # use pen default if node is not selected
        painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())

    def boundingRect(self):
        return QRectF(0, 0, 2 * self.edge_size + self.width, 2 * self.edge_size + self.height).normalized()

import math
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QLine
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPen
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRectF


class GraphEditorScene(QGraphicsScene):
    """
    The graphics scene the layout background for the editor window

    Attributes
    ----------
    _color_background : QColor
        The color of the background of the graphics Scene
    _gridSize: int
        Size of the large grid which will be drawn on top of the background color.
    _gridSquares: int
        Size of the smaller grids that will be inside of the grids of _gridSize
    _pen_light : QPen
        Used to draw the smaller grid squares on the graphics scene
    _pen_dark : QPen
        Used to draw the larger grid square on the scene
    """
    _color_background: QColor
    _gridSize: int
    _gridSquares: int
    _pen_light: QPen
    _pen_dark: QPen

    def __init__(self, scene_width, scene_height, parent=None):
        super().__init__(parent)

        # settings for the background
        self.scene_width, self.scene_height = scene_width, scene_height
        self.init_background_params()

    '''
        Sets parameters that will draw the grid background
    '''

    def init_background_params(self):
        # Size and color of the grid squares
        self._gridSize = 20
        self._gridSquares = 5
        self._color_background = QColor("#393939")
        self._color_light = QColor("2F2F2F")
        self._color_dark = QColor("292929")

        # Pens and widths to create the lines
        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)
        self.setBackgroundBrush(self._color_background)

        # sets scene rectangle
        self.setSceneRect(-self.scene_width // 2, -self.scene_height // 2, self.scene_width, self.scene_height)

    """
           Draws the grid of the graphics scene background.

           Parameters
           ----------
           painter : QPainter
               Performs low-level painting on widgets such as QPen for drawing the grid.
           rect : QRectF
               Defines a rectangle in the plane using floating point precision.
    """

    def drawBackground(self, painter: QPainter, rect: QRectF):
        super().drawBackground(painter, rect)

        # here we create our grid
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self._gridSize)
        first_top = top - (top % self._gridSize)

        # compute all lines to be drawn
        lines_light, lines_dark = [], []
        for x in range(first_left, right, self._gridSize):
            if (x % (self._gridSize * self._gridSquares) != 0):
                lines_light.append(QLine(x, top, x, bottom))
            else:
                lines_dark.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self._gridSize):
            if (y % (self._gridSize * self._gridSquares) != 0):
                lines_light.append(QLine(left, y, right, y))
            else:
                lines_dark.append(QLine(left, y, right, y))

        # draw the lines
        painter.setPen(self._pen_light)
        painter.drawLines(*lines_light)

        painter.setPen(self._pen_dark)
        painter.drawLines(*lines_dark)

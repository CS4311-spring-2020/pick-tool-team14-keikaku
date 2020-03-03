import math
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QLine
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPen
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRectF


class AttackGraphScence(QGraphicsScene):
    """
    The graphics scene that holds attack graph elements that are
    displayed to the user.

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

    def __init__(self, parent=None):
        """
        Initializer method for the AttackGraphScene

        Parameters
        ----------
        parent: QWidget
            parent widget
        """
        super().__init__(parent)

        # settings
        self._gridSize = 20
        self._gridSquares = 5
        self._color_background = QColor("#393939")
        self._color_light = QColor("2F2F2F")
        self._color_dark = QColor("292929")

        # For creating the grid
        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)

        # TODO make the scene size dynamic
        self.scene_width, self.scene_height = 64000, 64000

        # This is where the focus of the scene will be
        # TODO set this to the be where the las edited node is
        self.setSceneRect(-self.scene_width // 2, -self.scene_height // 2, self.scene_width, self.scene_height)

        self.setBackgroundBrush(self._color_background)

    def drawBackground(self, painter: QPainter, rect: QRectF):
        """
        Draws the grid of the graphics scene background.
        TODO fix background cache

        Parameters
        ----------
        painter : QPainter
            Performs low-level painting on widgets such as QPen for drawing the grid.
        rect : QRectF
            Defines a rectangle in the plane using floating point precision.
        """
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

import math
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QLine
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPen
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRectF


class NodeScene(QGraphicsScene):
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

    def __init__(self, parent=None):
        """
        Initializer method for the AttackGraphScene

        Parameters
        ----------
        parent: QWidget
            parent widget
        """
        super().__init__(parent)


    def drawBackground(self, painter: QPainter, rect: QRectF):
        """
        Draws the grid of the graphics scene background.

        Parameters
        ----------
        painter : QPainter
            Performs low-level painting on widgets such as QPen for drawing the grid.
        rect : QRectF
            Defines a rectangle in the plane using floating point precision.
        """
        super().drawBackground(painter, rect)


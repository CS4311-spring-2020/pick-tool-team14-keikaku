from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtGui import QPainter
from PyQt5.Qt import QGraphicsScene
from PyQt5.Qt import QWheelEvent
from src.gui.graph.graph_editor_scene import GraphEditorScene


class GraphEditorView(QGraphicsView):
    """
    GraphEditorView provides a widget for displaying the contents of a GraphScene.

    Attributes
    ----------
    graph_editor_scene : GraphEditorScene
       Class that provides a surface for managing a large number of 2D graphical items.
    """

    graph_editor_scene: GraphEditorScene

    def __init__(self, graph_editor_scene: GraphEditorScene, parent=None):
        super().__init__(parent)

        # get scene and initialize the graph view
        self.graph_editor_scene = graph_editor_scene
        self.setScene(self.graph_editor_scene)
        self.init_ui()

        # variables for zooming
        self.zoom_in_factor = 1.25
        self.zoom_clamp = False
        self.zoom = 5
        self.zoom_step = 1
        self.zoom_range = [0, 10]

    '''
    Sets graphics and general behavior of to graphics view.
    '''

    def init_ui(self):
        # # remove anti aliasing
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing |
                            QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        # Updates graphics so when they overlap they don't erase each other
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # tracks mouse position for zoom
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    '''
    Listen to QWheelEvent and handles zooming in and out of the given GraphEditorScene

    wheel_event: QWheelEvent
         Class that contains parameters that describe a wheel event.
    '''

    def wheelEvent(self, wheel_event: QWheelEvent):

        # calculate zoom factor
        zoom_out_factor = 1 / self.zoom_in_factor

        # calculate zoom
        if wheel_event.angleDelta().y() > 0:
            zoom_factor = self.zoom_in_factor
            self.zoom += self.zoom_step
        else:
            zoom_factor = zoom_out_factor
            self.zoom -= self.zoom_step

        # clap zoom factor
        clapped = False
        if self.zoom > self.zoom_range[1]:
            self.zoom = self.zoom_range[1]
            clapped = True
        if self.zoom < self.zoom_range[0]:
            self.zoom = self.zoom_range[0]
            clapped = True

        # set scene scale
        if not clapped:
            self.scale(zoom_factor, zoom_factor)

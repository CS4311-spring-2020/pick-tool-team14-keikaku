from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtGui import QPainter
from PyQt5.Qt import QMouseEvent
from PyQt5.Qt import QWheelEvent


class GraphEditorView(QGraphicsView):
    def __init__(self, background_scene, parent=None):
        super().__init__(parent)
        self.background_scene = background_scene
        self.init_ui()
        self.setScene(self.background_scene)

        # variables for zooming
        self.zoom_in_factor = 1.25
        self.zoom_clamp = False
        self.zoom = 5
        self.zoom_step = 1
        self.zoom_range = [0, 10]

    def init_ui(self):
        # # remove anti aliasing
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing |
                            QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        # Updates graphics so when they overlap they don't erase each other
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # tracks mouse position for zoom
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def wheelEvent(self, wheel_event : QWheelEvent):
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


        #set scene scale
        if not clapped :
            self.scale(zoom_factor, zoom_factor)



    # def mousePressEvent(self, mouse_event : QMouseEvent):
    #     if mouse_event.button() == Qt.MiddleButton:
    #         self.setDragMode(QGraphicsView.ScrollHandDrag)
    #     else:
    #         super().mousePressEvent(mouse_event)
    #
    # def mouseReleaseEvent(self, mouse_event : QMouseEvent):
    #     if mouse_event.button() == Qt.MiddleButton:
    #         self.setDragMode(QGraphicsView.ScrollHandDrag)
    #     else:
    #         super().mousePressEvent(mouse_event)

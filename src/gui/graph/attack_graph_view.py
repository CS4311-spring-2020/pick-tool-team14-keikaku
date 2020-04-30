from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtGui import QWheelEvent
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class AttackGraphView(QGraphicsView):

    def __init__(self, gr_scene: QGraphicsView, parent: QWidget = None):
        super().__init__(parent)

        self.grc_scene = gr_scene
        self._scroll_mode = False
        self.init_ui()
        self.setScene(self.grc_scene)

    def init_ui(self):
        # Sets up Aliasing
        self.setRenderHints(
            QPainter.Antialiasing | QPainter.HighQualityAntialiasing |
            QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)

        # Get full update of view instead of a cached view
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # Hide scroll bars
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


    def mousePressEvent(self, mouse_event : QMouseEvent):
        if mouse_event.button() == Qt.LeftButton:
            self.left_mouse_button_pressed(mouse_event)
        elif mouse_event.button() == Qt.RightButton:
            self.right_mouse_button_pressed(mouse_event)
        else:
            super().mousePressEvent(mouse_event)

    def mouseReleaseEvent(self, mouse_event : QMouseEvent):
        if mouse_event.button() == Qt.LeftButton:
            self.left_mouse_button_pressed(mouse_event)
        elif mouse_event.button() == Qt.RightButton:
            self.right_mouse_button_pressed(mouse_event)
        else:
            super().mousePressEvent(mouse_event)

    def mouseDoubleClickEvent(self, mouse_event : QMouseEvent):
        if self._scroll_mode:
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self._scroll_mode = not self._scroll_mode
        else:
            self.setDragMode(QGraphicsView.NoDrag)
            self._scroll_mode = not self._scroll_mode

    # def wheelEvent(self, wheel_event : QWheelEvent):
    #     # calculate our zoom Factor
    #     zoom_out_factor = 1 / self.zoom_in_factor
    #
    #     # calculate zoom
    #     if wheel_event.angleDelta().y() > 0:
    #         zoom_factor = self.zoom_in_factor
    #         self.zoom += self.zoomStep
    #     else:
    #         zoom_factor = zoom_out_factor
    #         self.zoom -= self.zoomStep
    #
    #     clamped = False
    #     if self.zoom < self.zoom_range[0]: self.zoom, clamped = self.zoom_range[0], True
    #     if self.zoom > self.zoom_range[1]: self.zoom, clamped = self.zoom_range[1], True
    #
    #     # set scene scale
    #     if not clamped or self.zoom_clamp is False:
    #         self.scale(zoom_factor, zoom_factor)

    def left_mouse_button_pressed(self, mouse_event : QMouseEvent):
        return super().mousePressEvent(mouse_event)

    def left_mouse_button_release(self, mouse_event : QMouseEvent):
        return super().mouseReleaseEvent(mouse_event)

    def right_mouse_button_pressed(self, mouse_event : QMouseEvent):
        return super().mousePressEvent(mouse_event)

    def right_mouse_button_release(self, mouse_event : QMouseEvent):
        return super().mouseReleaseEvent(mouse_event)






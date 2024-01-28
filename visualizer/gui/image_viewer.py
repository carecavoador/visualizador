from PySide6.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
)
from PySide6.QtGui import QImage
from PySide6.QtGui import Qt

from draggable_image import DraggableImage


class ImageViewer(QGraphicsView):
    def __init__(self) -> None:
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.scene.setBackgroundBrush(Qt.gray)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

    def load_image(self, image: QImage, inverted: bool = False) -> None:
        _new_image = DraggableImage(image.rect())

        pen = _new_image.pen()
        pen.setColor(Qt.red)
        pen.setWidth(2)
        _new_image.setPen(pen)

        if inverted:
            image.invertPixels()
            _new_image.setOpacity(0.5)

        brush = _new_image.brush()
        brush.setTextureImage(image)
        _new_image.setBrush(brush)

        self.scene.addItem(_new_image)

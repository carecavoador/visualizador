import sys
import copy

from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtCore import Qt, Signal, QRectF


# Test images
IMAGE_A = r"C:\Users\everton.souza\Desktop\test_image_a.jpg"
IMAGE_B = r"C:\Users\everton.souza\Desktop\test_image_b.jpg"


class KeyboardViewer(QGraphicsView):

    offset_direction = Signal(tuple)

    def __init__(self):
        super().__init__()

        self.setFocusPolicy(Qt.StrongFocus)  # Enable keyboard focus

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            direction = (-1, 0)
        elif event.key() == Qt.Key_Right:
            direction = (1, 0)
        elif event.key() == Qt.Key_Up:
            direction = (0, -1)
        elif event.key() == Qt.Key_Down:
            direction = (0, 1)

        if direction:
            self.offset_direction.emit(direction)


class DifferenceViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.image_a = QImage(IMAGE_A)
        self.image_b = QImage(IMAGE_B)
        self.composite_image = None

        self.scene = QGraphicsScene()
        self.view = KeyboardViewer()
        self.view.offset_direction.connect(self.offset_image_b)
        self.view.setScene(self.scene)
        self.view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.view.setRenderHint(QPainter.SmoothPixmapTransform)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.setMinimumSize(800, 600)
        self.setCentralWidget(self.view)

        self.show_differences()


    def offset_image_b(self, offset):
        print(offset)


    def show_differences(self):
        """
        Inverts `self.image_b` and blends it with 50% opacity over
        `self.image_a` making equal color pixels appear gray.
        """
        composite = copy.copy(self.image_a)

        other = copy.copy(self.image_b)
        other.invertPixels()

        painter = QPainter()
        painter.begin(composite)
        painter.setOpacity(0.5)
        painter.drawImage(0, 0, other)
        painter.end()

        self.composite_image = composite
        self.display_image(composite)


    def display_image(self, image: QImage):
        """
        This method cleans `sef.scene` and displays a new image. It's not
        really necessary in this example, but I decided to include it anyway...
        """
        self.scene.clear()
        self.view.update()
        pixmap = QPixmap.fromImage(image)
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.view.setSceneRect(QRectF(pixmap.rect()))
        self.view.setScene(self.scene)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = DifferenceViewer()
    viewer.show()
    sys.exit(app.exec())

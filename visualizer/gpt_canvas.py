from PySide6.QtWidgets import (
    QApplication,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsPixmapItem,
    QGraphicsItem,
    QGraphicsRectItem,
)
from PySide6.QtGui import QPixmap, QPainter, Qt, QImage

import sys


class DraggableRectItem(QGraphicsRectItem):
    def __init__(self, rec):
        super().__init__(rec)

    def mousePressEvent(self, event):
        # Save the initial position when the mouse is pressed
        self.start_pos = event.scenePos()

    def mouseMoveEvent(self, event):
        # Calculate the movement delta
        delta = event.scenePos() - self.start_pos

        # Update the position of the rectangle
        self.setPos(self.pos() + delta)

        # Update the start position for the next movement
        self.start_pos = event.scenePos()

    def mouseReleaseEvent(self, event):
        # Do something when the mouse is released (optional)
        pass


class ImageViewer(QGraphicsView):
    def __init__(self):
        super().__init__()

        # Create a QGraphicsScene and set it as the scene for the view
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Set the background color of the scene (optional)
        self.scene.setBackgroundBrush(self.palette().window())

        # Set up the view
        self.setRenderHint(QPainter.Antialiasing, True)
        self.setRenderHint(QPainter.SmoothPixmapTransform, True)
        self.setRenderHint(QPainter.TextAntialiasing, True)

        # Load and display an image (you can replace 'your_image.jpg' with the actual image file)
        # self.load_image(r'C:\python\visualizador\visualizador\test_image_a.jpg')

        self.setSceneRect(0, 0, 1024, 1024)

        self.draw_rectangle(
            r"C:\Users\erodr\Desktop\Python\visualizador\visualizer\test_image_a.jpg"
        )
        self.draw_rectangle(
            r"C:\Users\erodr\Desktop\Python\visualizador\visualizer\test_image_b.jpg",
            "b",
        )

    def load_image(self, filename):
        # Create a QGraphicsPixmapItem to display the image
        pixmap = QPixmap(filename)
        item = QGraphicsPixmapItem(pixmap)

        # Add the item to the scene
        self.scene.addItem(item)

        # Fit the view to the image size
        self.setSceneRect(item.pixmap().rect())

    def draw_rectangle(self, img, t="a"):
        imagem = QImage(img)

        # Create a QGraphicsRectItem (rectangle item)
        rect_item = DraggableRectItem(imagem.rect())  # x, y, width, height

        # Set the pen (border) and brush (fill) for the rectangle
        pen = rect_item.pen()
        pen.setColor(Qt.red)
        pen.setWidth(2)
        rect_item.setPen(pen)

        brush = rect_item.brush()
        # brush.setColor(Qt.green)
        # brush.setStyle(Qt.SolidPattern)
        if t == "b":
            imagem.invertPixels()
            # imagem.
            rect_item.setOpacity(0.5)
        brush.setTextureImage(imagem)
        rect_item.setBrush(brush)

        # Add the rectangle item to the scene
        self.scene.addItem(rect_item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())

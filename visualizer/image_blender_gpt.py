import sys
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QImage, QImageReader, QImageWriter
from PySide6.QtCore import Qt, QPointF

class ImageBlenderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Image Blender")
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Create two QGraphicsView widgets for displaying images
        self.view1 = QGraphicsView(self)
        self.view2 = QGraphicsView(self)

        layout.addWidget(self.view1)
        layout.addWidget(self.view2)

        # Create QGraphicsScene for each view
        self.scene1 = QGraphicsScene(self)
        self.scene2 = QGraphicsScene(self)

        self.view1.setScene(self.scene1)
        self.view2.setScene(self.scene2)

        # Create QLabel to display blending result
        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        # Load images when the app starts
        self.load_image1(r"C:\Users\everton.souza\python\visualizador\tests\sample_images\test_image_a.jpg")
        self.load_image2(r"C:\Users\everton.souza\python\visualizador\tests\sample_images\test_image_b.jpg")

    def load_image1(self, filename):
        # Load the first image
        image = QImageReader(filename).read()
        self.image1 = QPixmap.fromImage(image)

        # Display the image in the first QGraphicsView
        self.item1 = QGraphicsPixmapItem(self.image1)
        self.scene1.addItem(self.item1)

    def load_image2(self, filename):
        # Load the second image
        image = QImageReader(filename).read()
        self.image2 = QPixmap.fromImage(image)

        # Display the image in the second QGraphicsView
        self.item2 = QGraphicsPixmapItem(self.image2)
        self.scene2.addItem(self.item2)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # Save the initial position of the second image
            self.initial_pos = self.item2.pos()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'initial_pos'):
            # Calculate the new position of the second image based on mouse movement
            delta = event.pos() - event.lastPos()
            self.item2.setPos(self.initial_pos + delta)

    def mouseReleaseEvent(self, event):
        if hasattr(self, 'initial_pos'):
            delattr(self, 'initial_pos')
        self.blend_images()

    def blend_images(self):
        # Get the positions of the two images
        pos1 = self.item1.pos()
        pos2 = self.item2.pos()

        # Create a blank image with the same size as the first image
        result_image = QImage(self.image1.size(), QImage.Format.Format_RGB32)
        result_image.fill(Qt.GlobalColor.white)

        # Calculate the position of the second image in the result image
        offset = QPointF(pos2 - pos1)

        # Draw the first image onto the result image
        painter = QPainter(result_image)
        painter.drawPixmap(offset, self.image1)

        # Blend the second image onto the result image using alpha blending
        painter.setOpacity(0.5)  # Adjust the opacity as needed
        painter.drawPixmap(offset, self.image2)

        # Display the blended image
        self.result_label.setPixmap(QPixmap.fromImage(result_image))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageBlenderApp()
    window.show()
    sys.exit(app.exec())

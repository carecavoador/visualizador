import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QImage, QPixmap, QPainter, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog

class ImageDragApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Image Dragging App")
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.image_label)

        self.image_pixmap = None
        self.image_position = QPoint(0, 0)
        self.dragging = False

        self.initMenu()

    def initMenu(self):
        open_action = self.createAction("Open", self.openImage)
        self.statusBar()

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction(open_action)

    def createAction(self, text, slot):
        action = QAction(text, self)
        action.triggered.connect(slot)
        return action

    def openImage(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image File", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options
        )

        if file_name:
            self.image_pixmap = QPixmap(file_name)
            self.image_label.setPixmap(self.image_pixmap)
            self.image_label.resize(self.image_pixmap.size())
            self.image_position = QPoint(0, 0)
            self.dragging = False

    def mousePressEvent(self, event):
        if self.image_pixmap and event.button() == Qt.LeftButton:
            if self.image_label.geometry().contains(event.pos()):
                self.dragging = True
                self.drag_start_position = event.pos() - self.image_position

    def mouseMoveEvent(self, event):
        if self.dragging:
            new_position = event.pos() - self.drag_start_position
            if self.isPositionValid(new_position):
                self.image_position = new_position
                self.update()

    def mouseReleaseEvent(self, event):
        if self.dragging:
            self.dragging = False

    def isPositionValid(self, position):
        return (
            position.x() >= 0
            and position.x() <= self.image_label.width() - self.image_pixmap.width()
            and position.y() >= 0
            and position.y() <= self.image_label.height() - self.image_pixmap.height()
        )

    def paintEvent(self, event):
        if self.image_pixmap:
            painter = QPainter(self)
            painter.drawPixmap(self.image_position, self.image_pixmap)

def main():
    app = QApplication(sys.argv)
    window = ImageDragApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

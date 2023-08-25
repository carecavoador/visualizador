from pathlib import Path

from PySide6.QtWidgets import (
    QMainWindow,
    QGraphicsView,
    QGraphicsScene,
    QFileDialog,
    QGraphicsPixmapItem,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtGui import QPixmap, QImageReader, QImage, QAction, QPainter
from PySide6.QtCore import QRectF


# Test images
IMAGE_A = (
    Path(__file__)
    .parent.parent.joinpath("tests/sample_images/test_image_a.jpg")
    .as_posix()
)
IMAGE_B = (
    Path(__file__)
    .parent.parent.joinpath("tests/sample_images/test_image_b.jpg")
    .as_posix()
)

# Disable the file size limit to open images.
QImageReader.setAllocationLimit(0)


class DifferenceViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)

        self.initUI()
        self.open_image()

    def initUI(self):
        self.setWindowTitle("Visualizador de diferenças v0.1")
        self.setGeometry(100, 100, 800, 600)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        # self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.view.setRenderHint(QPainter.SmoothPixmapTransform)
        self.view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        layout = QVBoxLayout()
        layout.addWidget(self.view)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        self.create_actions()
        self.create_menus()

    def create_actions(self):
        # Open image
        self.open_action = QAction("Abrir Imagem...", self)
        self.open_action.triggered.connect(self.open_image)

        # Zoom in
        self.zoom_in_action = QAction("Aumentar Zoom", self)
        self.zoom_in_action.setShortcut("=")
        self.zoom_in_action.triggered.connect(self.zoom_in)

        # Actual size
        self.zoom_actual_action = QAction("Zoom 100%", self)
        self.zoom_actual_action.setShortcut("0")
        self.zoom_actual_action.triggered.connect(self.zoom_actual)

        # Zoom out
        self.zoom_out_action = QAction("Diminuir Zoom", self)
        self.zoom_out_action.setShortcut("-")
        self.zoom_out_action.triggered.connect(self.zoom_out)

    def create_menus(self):
        self.file_menu = self.menuBar().addMenu("Imagem")
        self.file_menu.addAction(self.open_action)

        self.view_menu = self.menuBar().addMenu("Zoom")
        self.view_menu.addAction(self.zoom_in_action)
        self.view_menu.addAction(self.zoom_out_action)
        self.view_menu.addAction(self.zoom_actual_action)

    def open_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        # file_name, _ = QFileDialog.getOpenFileName(
        #     self,
        #     "Abrir Imagem",
        #     "",
        #     "Imagens (*.png *.xpm *.jpg *.bmp);;Todos os arquivos (*)",
        #     options=options,
        # )

        # Test Image
        # file_name = r"C:\Users\everton.souza\python\visualizador\visualizador\test_image_a.jpg"
        file_name = IMAGE_A

        if file_name:
            imagem = QImage(IMAGE_A)
            imagem_b = QImage(IMAGE_B)
            imagem_b.invertPixels()
            p = QPainter()
            p.begin(imagem)
            # p.setCompositionMode(p.CompositionMode.CompositionMode_Difference)
            p.setOpacity(0.5)
            p.drawImage(0, 0, imagem_b)
            p.end()
            # image = QImage(file_name)
            # pixmap = QPixmap.fromImage(image)
            pixmap = QPixmap.fromImage(imagem)
            item = QGraphicsPixmapItem(pixmap)
            self.scene.clear()
            self.scene.addItem(item)
            self.view.setSceneRect(QRectF(pixmap.rect()))
            self.view.setScene(self.scene)

    def zoom_in(self):
        self.view.scale(1.2, 1.2)

    def zoom_out(self):
        self.view.scale(1 / 1.2, 1 / 1.2)

    def zoom_actual(self):
        self.view.resetTransform()

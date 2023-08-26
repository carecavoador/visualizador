from pathlib import Path
from copy import copy
from PySide6.QtWidgets import (
    QMainWindow,
    QGraphicsView,
    QGraphicsScene,
    QFileDialog,
    QGraphicsPixmapItem
)
from PySide6.QtGui import QPixmap, QImageReader, QImage, QAction, QPainter
from PySide6.QtCore import QRectF
from visualizador.gui.difference_viewer import Ui_DifferenceViewer


# Test images
IMAGE_A = (
    Path(__file__)
    .parent.parent.parent.joinpath("tests/sample_images/test_image_a.jpg")
    .as_posix()
)
IMAGE_B = (
    Path(__file__)
    .parent.parent.parent.joinpath("tests/sample_images/test_image_b.jpg")
    .as_posix()
)

# Disable the file size limit to open images.
QImageReader.setAllocationLimit(0)


class DifferenceViewer(Ui_DifferenceViewer, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.image_a = None
        self.image_b = None
        self.composite_image = None

        # Zoom in action
        self.zoom_in_action = QAction("Aumentar Zoom", self)
        self.zoom_in_action.setShortcut("=")
        self.zoom_in_action.triggered.connect(self.zoom_in)

        # Zoom out action
        self.zoom_out_action = QAction("Diminuir Zoom", self)
        self.zoom_out_action.setShortcut("-")
        self.zoom_out_action.triggered.connect(self.zoom_out)

        # Zoom reset action
        self.zoom_actual_action = QAction("Resetar Zoom", self)
        self.zoom_actual_action.setShortcut("0")
        self.zoom_actual_action.triggered.connect(self.zoom_reset)

        # Buttons
        self.btn_zoom_in.clicked.connect(self.zoom_in)
        self.btn_zoom_out.clicked.connect(self.zoom_out)
        self.btn_zoom_reset.clicked.connect(self.zoom_reset)
        self.btn_img_a.clicked.connect(self.load_image_a)
        self.btn_img_b.clicked.connect(self.load_image_b)
        self.btn_export.clicked.connect(self.export_image)

        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.view.setRenderHint(QPainter.SmoothPixmapTransform)
        self.view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

    def get_filename(self) -> str:
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir Imagem",
            "",
            "Imagens (*.jpg *.png *.tif *.bmp);;Todos os arquivos (*)",
            options=options,
        )
        return file_name

    def load_image_a(self):
        file_name = self.get_filename()
        if file_name:
            self.image_a = QImage(file_name)
            self.edit_img_a.setText(file_name)
        if self.image_b is not None:
            self.show_differences()
        else:
            self.display_image(self.image_a)

    def load_image_b(self):
        file_name = self.get_filename()
        if file_name:
            self.image_b = QImage(file_name)
            self.edit_img_b.setText(file_name)

        if self.image_a is not None:
            self.show_differences()
        else:
            self.display_image(self.image_b)

    def export_image(self) -> None:
        caminho = r"C:\Users\erodr\Python\visualizador\visualizador\teste.png"
        self.composite_image.save(caminho)

    def show_differences(self):
        composite = copy(self.image_a)
        other = copy(self.image_b)
        other.invertPixels()
        painter = QPainter()
        painter.begin(composite)
        # p.setCompositionMode(p.CompositionMode.CompositionMode_Difference)
        painter.setOpacity(0.5)
        painter.drawImage(0, 0, other)
        painter.end()
        self.composite_image = composite
        self.display_image(composite)

    def display_image(self, image: QImage):            
        self.scene.clear()
        self.view.update()
        pixmap = QPixmap.fromImage(image)
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.view.setSceneRect(QRectF(pixmap.rect()))
        self.view.setScene(self.scene)

    def zoom_in(self):
        self.view.scale(1.2, 1.2)

    def zoom_out(self):
        self.view.scale(1 / 1.2, 1 / 1.2)

    def zoom_reset(self):
        self.view.resetTransform()

from pathlib import Path

from icecream import ic

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QToolBar,
    QWidget,
    QFileDialog,
    QGraphicsView,
    QGraphicsScene,
    QLabel,
)
from PySide6.QtGui import QAction, QImage

from image_viewer import ImageViewer


FILE_FILTERS = ["Imagem JPEG (*.jpg)", "Imagem PNG (*.png)", "Todos arquivos (*)"]


class VisualizerMainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Configure the main window
        self.setWindowTitle("Visualizador de diferenças")
        self.setMinimumSize(1024, 1024)
        viewport = QWidget()
        viewport_layout = QVBoxLayout()
        viewport.setLayout(viewport_layout)

        # Configure the main toolbar
        main_toolbar = QToolBar("Main toolbar")
        btn_load_image_a = QAction("Carregar Imagem A", self)
        btn_load_image_a.triggered.connect(self.load_image_a)
        btn_load_image_b = QAction("Carregar Imagem B", self)
        btn_load_image_b.triggered.connect(self.load_image_b)
        main_toolbar.addAction(btn_load_image_a)
        main_toolbar.addAction(btn_load_image_b)
        self.addToolBar(main_toolbar)

        # Configure the image viewer
        self.viewer = ImageViewer()
        viewport_layout.addWidget(self.viewer)

        self.setCentralWidget(viewport)


    def load_image_dialog(self) -> str:
        file_filters = ";;".join(FILE_FILTERS)
        image_path, extension = QFileDialog.getOpenFileName(
            self,
            filter=file_filters,
        )
        return image_path


    def load_image_a(self) -> None:
        image_path = self.load_image_dialog()
        if not image_path:
            return
        new_image = QImage(image_path)
        self.viewer.load_image(new_image)


    def load_image_b(self) -> None:
        image_path = self.load_image_dialog()
        if not image_path:
            return
        new_image = QImage(image_path)
        self.viewer.load_image(new_image, inverted=True)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    main_window = VisualizerMainWindow()
    main_window.show()
    sys.exit(app.exec())

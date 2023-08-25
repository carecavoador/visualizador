import sys

from PySide6.QtWidgets import QApplication

from viewer import DifferenceViewer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = DifferenceViewer()
    viewer.show()
    sys.exit(app.exec())

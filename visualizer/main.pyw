#!C:\\Users\\everton.souza\\AppData\\Local\\pypoetry\\Cache\\virtualenvs\\visualizador-DqT34PtS-py3.11\\Scripts\\pythonw.exe

import sys
from PySide6.QtWidgets import QApplication
from visualizador.gui.viewer_window import DifferenceViewer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = DifferenceViewer()
    viewer.show()
    sys.exit(app.exec())

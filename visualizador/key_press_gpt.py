import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setFocusPolicy(Qt.StrongFocus)  # Enable keyboard focus

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            print("Left arrow key pressed")
        elif event.key() == Qt.Key_Right:
            print("Right arrow key pressed")
        elif event.key() == Qt.Key_Up:
            print("Up arrow key pressed")
        elif event.key() == Qt.Key_Down:
            print("Down arrow key pressed")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Arrow Key Monitor")
        self.setGeometry(100, 100, 400, 300)

        central_widget = CustomWidget()
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

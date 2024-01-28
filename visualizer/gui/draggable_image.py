from PySide6.QtWidgets import QGraphicsRectItem


class DraggableImage(QGraphicsRectItem):
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

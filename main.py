from PyQt5.QtWidgets import (QApplication, QGraphicsScene,
                             QGraphicsRectItem, QGraphicsView, QGraphicsItem)
from PyQt5.QtCore import qDebug, Qt, QTimer
import sys


# 3 coordinates to keep track off
# scene - gets bigger as more objects are added (or as objects get bigger)
# view - as scene gets bigger, view develops scrollbars to see
#                              other areas of the view 
# myrect


class MyRect(QGraphicsRectItem):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Left:
            self.setPos(self.x() - 10, self.y())
        elif e.key() == Qt.Key_Right:
            self.setPos(self.x() + 10, self.y())
        elif e.key() == Qt.Key_Up:
            self.setPos(self.x(), self.y() - 10)
        elif e.key() == Qt.Key_Down:
            self.setPos(self.x(), self.y() + 10)
        elif e.key() == Qt.Key_Space:
            bullet = Bullet()
            self.scene().addItem(bullet)


class Bullet(QGraphicsRectItem):
    def __init__(self):
        super().__init__()
        self.setRect(0, 0, 10, 10)
        self.timer = QTimer()
        self.timer.timeout.connect(self.move)
        self.timer.start(50)

    def move(self):
        # move the bullet up
        self.setPos(self.x(), self.y() - 10)


if __name__ == '__main__':
    try:
        if app:
            pass
    except:
        app = QApplication(sys.argv)
        print("app exists")

    # Create a scene
    scene = QGraphicsScene()

    # Create an item to add to the scene
    rect = MyRect()
    rect.setRect(0, 0, 100, 100)
    # Item needs to focused to see keyevents
    rect.setFlag(QGraphicsItem.ItemIsFocusable, True)
    rect.setFocus()

    # Add the item to the scene
    scene.addItem(rect)

    # Show the scene
    # First the view widget gets the event, which sends it to the scene
    # The scene sends the event to the item in focus
    view = QGraphicsView(scene)
    view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    view.setFixedSize(800, 600)
    scene.setSceneRect(0, 0, 600, 800)

    app.exec_()

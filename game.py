from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtCore import Qt, QTimer
import random
import gui


# 3 coordinates to keep track off
# scene - gets bigger as more objects are added (or as objects get bigger)
# view - as scene gets bigger, view develops scrollbars to see
# other areas of the view
# myrect
class MyRect(QGraphicsRectItem):
    def __init__(self, score):
        super().__init__()
        self.enemies = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.spawnEnemy)
        self.timer.start(1000)
        self.motion = 0
        self.moveTimer = QTimer()
        self.moveTimer.timeout.connect(self.move)
        self.moveTimer.start(50)
        self.score = score

    def move(self):
        self.setPos(self.x() + 10*self.motion, self.y())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Left:
            if self.pos().x() > 0:
                self.motion = -1

        elif e.key() == Qt.Key_Right:
            if self.pos().x() + self.rect().width() < 800:
                self.motion = 1

        if e.key() == Qt.Key_Space:
            bullet = Bullet(self.score)
            bullet.setPos(
                self.x() + self.rect().width()/2 -
                bullet.rect().width()/2, self.y())
            self.scene().addItem(bullet)

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_Left:
            if self.motion != 1:
                self.motion = 0

        elif e.key() == Qt.Key_Right:
            if self.motion != -1:
                self.motion = 0

    def spawnEnemy(self):
        self.scene().addItem(Enemy())


class Bullet(QGraphicsRectItem):
    def __init__(self, score):
        super().__init__()
        self.setRect(0, 0, 10, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.move(score))
        self.timer.start(50)

    def move(self, score):
        # If the bullet collides with the enemy destroy both
        collidingItems = self.collidingItems()

        for item in collidingItems:
            if isinstance(item, Enemy):
                self.scene().removeItem(item)
                self.scene().removeItem(self)
                self.timer.stop()
                del item
                del self
                score.increase()
                return

        # move # TODO: he bullet up
        self.setPos(self.x(), self.y() - 10)
        if self.pos().y() < 0:
            self.scene().removeItem(self)
            self.timer.stop()
            del self


class Enemy(QGraphicsRectItem):
    def __init__(self):
        super().__init__()
        self.setRect(0, 0, 100, 100)
        # set random position
        random_number = random.randint(0, 800 - self.rect().width())
        self.setPos(random_number, 0)
        # connect
        self.timer = QTimer()
        self.timer.timeout.connect(self.move)
        self.timer.start(50)

    def move(self):
        self.setPos(self.x(), self.y() + 3)


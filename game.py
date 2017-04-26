import PyQt5.QtMultimedia as M
from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsPixmapItem
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtGui import QPixmap
import random


# 3 coordinates to keep track off
# scene - gets bigger as more objects are added (or as objects get bigger)
# view - as scene gets bigger, view develops scrollbars to see
# other areas of the view
# myrect
class MyRect(QGraphicsRectItem):
    def __init__(self, scene, score, health):
        super().__init__()
        scene.addItem(self)
        self.motion = 0
        self.moveTimer = QTimer()
        self.moveTimer.timeout.connect(self.move)
        self.moveTimer.start(50)
        self.score = score
        self.health = health
        self.timer = QTimer()
        self.timer.timeout.connect(self.spawnEnemy)
        self.timer.start(1000)
        url = QUrl.fromLocalFile("./res/sounds/bullet.mp3")
        media = M.QMediaContent(url)
        self.bulletSound = M.QMediaPlayer()
        self.bulletSound.setMedia(media)

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
            if Bullet.bullets > 0:
                Bullet.bullets -= 1
                print(Bullet.bullets)

                if self.bulletSound.state() == M.QMediaPlayer.PlayingState:
                    self.bulletSound.setPosition(0)
                elif self.bulletSound.state() == M.QMediaPlayer.StoppedState:
                    self.bulletSound.play()

                bullet = Bullet(self.score)
                bullet.setPos(
                    self.x() + self.rect().width()/2 -
                    bullet.rect().width()/2, self.y())
                self.scene().addItem(bullet)
            else:
                print("no bullets")

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_Left:
            if self.motion != 1:
                self.motion = 0

        elif e.key() == Qt.Key_Right:
            if self.motion != -1:
                self.motion = 0

    def spawnEnemy(self):
        self.scene().addItem(Enemy(self.health))


class Bullet(QGraphicsPixmapItem):
    bullets = 3

    def __init__(self, score):
        super().__init__()
        # self.setRect(0, 0, 10, 30)
        self.setPixmap(QPixmap("./images/jorge.png"))
        self.timer = QTimer()
        self.timer.timeout.connect(self.move)
        self.timer.start(50)
        self.score = score


    def move(self):
        # If the bullet collides with the enemy destroy both
        collidingItems = self.collidingItems()

        for item in collidingItems:
            if isinstance(item, Enemy):
                Bullet.bullets += 1
                self.score.increase()
                self.scene().removeItem(item)
                self.scene().removeItem(self)
                return

        self.setPos(self.x(), self.y() - 10)
        if self.pos().y() < 0:
            Bullet.bullets += 1
            self.scene().removeItem(self)


class Enemy(QGraphicsRectItem):
    def __init__(self, health):
        super().__init__()
        self.health = health
        self.setRect(0, 0, 100, 100)
        # set random position
        random_number = random.randint(0, 800 - self.rect().width())
        self.setPos(random_number, 0)
        # connect
        self.timer = QTimer()
        self.timer.timeout.connect(self.move)
        self.timer.start(50)

    def move(self):
        if self.pos().y() > (600 - self.rect().height()):
            self.health.decrease()
            self.scene().removeItem(self)
            return

        collidingItems = self.collidingItems()
        for item in collidingItems:
            if isinstance(item, MyRect):
                self.health.decrease()
                self.scene().removeItem(self)
                return

        self.setPos(self.x(), self.y() + 3)

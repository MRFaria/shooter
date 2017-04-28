from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal


class Score(QGraphicsTextItem):
    def __init__(self, scene, parent=None):
        super().__init__(parent)
        scene.addItem(self)
        self._score = 0
        self.setFont(QFont("Arial", 15))
        self.setPlainText("Score: " + str(self._score))
        self.setDefaultTextColor(Qt.blue)

    def increase(self):
        self._score += 1
        self.setPlainText("Score: " + str(self._score))


class Health(QGraphicsTextItem):
    dead = pyqtSignal()

    def __init__(self, scene, parent=None):
        super().__init__(parent)
        scene.addItem(self)
        self._health = 1
        self.setFont(QFont("Arial", 15))
        self.setPlainText("Health: " + str(self._health))
        self.setDefaultTextColor(Qt.red)
        rect = self.boundingRect()
        self.setPos((800/2) - rect.width()/2, self.y())

    def decrease(self):
        self._health -= 1
        self.setPlainText("Health: " + str(self._health))
        if self._health <= 0:
            self.dead.emit()


class GameOver(QGraphicsTextItem):
    def __init__(self, scene, parent=None):
        super().__init__(parent)
        scene.addItem(self)
        self.setPlainText("GameOver")
        self.setDefaultTextColor(Qt.red)
        self.setFont(QFont("Arial", 50))
        rect = self.boundingRect()
        self.setPos((800/2) - rect.width()/2, self.y())
        print(self.boundingRect(), rect.width())

from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont


class Score(QGraphicsTextItem):
    def __init__(self, scene):
        super().__init__()
        scene.addItem(self)
        self._score = 0
        self.setPlainText("Score: " + str(self._score))
        self.setDefaultTextColor(Qt.blue)

    def increase(self):
        self._score += 1
        self.setPlainText("Score: " + str(self._score))


class Health(QGraphicsTextItem):
    def __init__(self, scene):
        super().__init__()
        scene.addItem(self)
        self._health = 5
        self.setPlainText("Health: " + str(self._health))
        self.setDefaultTextColor(Qt.red)
        self.setPos(self.pos().x() + 50, self.y())

    def decrease(self):
        self._health -= 1
        self.setPlainText("Health: " + str(self._health))

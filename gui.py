from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont


class Score(QGraphicsTextItem):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._score = 0
        self.setPlainText("Score: " + str(self._score))
        self.setDefaultTextColor(Qt.blue)
        self.setFont(QFont("times", 16))
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

    def increase(self):
        self._score += 1

    def update(self):
        self.setPlainText("Score: " + str(self._score))        


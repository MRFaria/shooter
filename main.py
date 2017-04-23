from PyQt5.QtWidgets import (QApplication, QGraphicsScene,
                             QGraphicsView, QGraphicsItem)
from PyQt5.QtCore import Qt
from PyQt5.QtOpenGL import QGLWidget
import sys
import game
import gui


if __name__ == '__main__':
    try:
        if app:
            pass
    except NameError:
        app = QApplication(sys.argv)
        print("app exists")

    # Create a scene
    scene = QGraphicsScene()
    # Create an item to add to the scene
    score = gui.Score(scene)
    health = gui.Health(scene)
    player = game.MyRect(scene, score, health)
    player.setRect(0, 0, 100, 100)
    # Item needs to focused to see keyevents
    player.setFlag(QGraphicsItem.ItemIsFocusable, True)
    player.setFocus()

    # Show the scene
    # First the view widget gets the event, which sends it to the scene
    # The scene sends the event to the item in focus
    view = QGraphicsView(scene)
    view.setViewport(QGLWidget())
    view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    view.setFixedSize(800, 600)
    scene.setSceneRect(0, 0, 800, 600)

    player.setPos(view.width()/2, view.height() - player.rect().height())
    view.show()

    app.exec_()

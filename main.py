import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from random import randrange, choice

COLORS = [(168, 54, 50), (232, 129, 44), (232, 210, 44), (100, 191, 48),
          (34, 138, 52), (39, 171, 160), (34, 78, 161), (92, 35, 158)]


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.start_drawing)
        self.paint_flag = False

    def paintEvent(self, event):
        if self.paint_flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def start_drawing(self):
        self.paint_flag = True
        self.repaint()

    def draw_circle(self, qp):
        width = randrange(10, 100, 10)
        x, y = randrange(100, 400, 20), randrange(100, 300, 20)
        color = choice(COLORS)
        qp.setBrush(QColor(color[0], color[1], color[2]))
        qp.drawEllipse(x, y, width, width)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
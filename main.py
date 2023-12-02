import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(860, 490, 400, 300)
        self.circle = False
        self.coordinates = (0, 0)
        self.pushbutton = QPushButton('Начерти уже этот круг!', self)
        self.pushbutton.setGeometry(200, 150, 200, 50)
        self.pushbutton.clicked.connect(self.run)

    def paintEvent(self, event):
        qp = QPainter()

        qp.begin(self)
        size = float(randint(20, 100))
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.coordinates = (randint(0, 400), randint(0, 300))
        if self.circle:
            qp.drawEllipse(QPoint(*self.coordinates), size, size)
            self.circle = False

    def run(self):
        self.circle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

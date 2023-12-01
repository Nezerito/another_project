import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.circle = False
        self.triangle = False
        self.rectangle = False
        self.coordinates = (0, 0)

    def paintEvent(self, event):
        qp = QPainter()

        qp.begin(self)
        size = float(randint(20, 100))
        qp.setBrush(QColor(224, 233, 30))
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

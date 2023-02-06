import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('circle.ui', self)
        self.setWindowTitle('Circle')
        self.pushButton.clicked.connect(self.click)
        self.show()
        self.check = False

    def click(self):
        self.check = True
        self.update()

    def paintEvent(self, event):
        if self.check:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            r = randint(10, 200)
            x, y = self.size().width(), self.size().height()
            qp.drawEllipse((x - r) // 2, (y - r) // 2, r, r)
            qp.end()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

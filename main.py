import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(472, 376)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 310, 171, 51))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Создать"))



class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.colors = {
            1: Qt.yellow,
            2: Qt.red,
            3: Qt.black,
            4: Qt.blue,
            5: Qt.green
        }
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
            color = self.colors.get(randint(1, 5))
            qp.setPen(QPen(color, 8, Qt.SolidLine))
            qp.setBrush(QBrush(color, Qt.SolidPattern))
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

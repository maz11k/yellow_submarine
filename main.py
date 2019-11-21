import sys
from random import randint
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush


class Example(QMainWindow, QWidget, QPainter, QColor):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Третья программа')
        self.btn = QPushButton('Создать жёлтый круг', self)
        self.btn.resize(150, 41)
        self.btn.move(180, 370)
        self.x = 0
        self.btn.clicked.connect(self.run)

    def run(self):
        self.x = randint(10, 300)

    def paintEvent(self, *args, **kwargs):
        qp = QPainter()
        qp.begin(self)
        col = QColor(0, 0, 0)
        col.setNamedColor('#ffcc00')
        qp.setPen(col)
        qp.setBrush(QColor(255, 204, 0))
        qp.drawEllipse(200, 100, self.x, self.x)
        self.update()
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

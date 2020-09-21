from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 300)
        # self.setWindowIcon(QIcon(""))
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.mainLayout = QVBoxLayout()


def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

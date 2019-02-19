import analytic
from PyQt5.QtWidgets import *
from StatMainWindow import Ui_MainWindow
import sys


class WindowInterface(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.analyser = analytic.Analytic(self)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Python-stat")

    window = WindowInterface()
    WindowInterface()

    sys.exit(app.exec_())

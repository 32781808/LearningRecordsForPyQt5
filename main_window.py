import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

# from FirstGUIWindow import *
from ExpressQuery import Ui_mainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.setFixedSize(mainWindow.width(), mainWindow.height())
    mainWindow.show()
    sys.exit(app.exec_())
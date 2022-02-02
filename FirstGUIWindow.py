import sys
from PyQt5.QtWidgets import QMainWindow


class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()

        self.setWindowTitle("第一个PyQt5GUI界面")
        self.resize(400, 300)
        self.status = self.statusBar()
        self.status.showMessage("消息只存在5s", 5000)

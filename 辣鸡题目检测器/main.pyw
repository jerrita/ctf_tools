import sys

# if hasattr(sys, 'frozen'):
#     os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from gui import *
import requests


class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setupUi(self)

    def broBtnClicked(self):
        addr = QFileDialog.getOpenFileUrl()
        self.lineEdit.setText(addr[0].url().split('///')[1])

    def goBtnClicked(self):
        addr = self.lineEdit.text()
        try:
            f = open(addr, 'rb').read().split(b'flag{')[1].split(b'}')[0]
            self.textEdit.setPlainText('恭喜你，这是道辣鸡题目，这是你的flag：\n\nflag{' + f.decode() + '}')
        except Exception:
            self.textEdit.setPlainText('您好，这似乎并不是一道辣鸡题目哦~')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWidget()
    myWin.show()
    sys.exit(app.exec_())

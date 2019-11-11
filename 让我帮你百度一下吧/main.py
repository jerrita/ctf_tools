import sys
from urllib.request import quote
import requests

# if hasattr(sys, 'frozen'):
#     os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QWidget
from gui import *


class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

    def goBtnClicked(self):
        if self.checkBox.isChecked():
            que = requests.get('http://suo.la/api.asp?url=http://www.iwo.im/?q='+self.lineEdit.text()).text
        else:
            que = 'http://www.iwo.im/?q=' + quote(self.lineEdit.text())
        self.lineEdit_2.setText(que)

    def copyBtnClicked(self):
        url = self.lineEdit_2.text()
        clipborad = QApplication.clipboard()
        clipborad.setText(url)
        self.statusShow.setText('复制成功！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWidget()
    myWin.show()
    sys.exit(app.exec_())

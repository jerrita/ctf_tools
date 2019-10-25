import sys

# if hasattr(sys, 'frozen'):
#     os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from gui import *
import requests


class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setupUi(self)

    def go_clicked(self):
        get = self.getEdit.toPlainText()
        post = self.postEdit.toPlainText()
        head = self.headEdit.toPlainText()
        url = self.urlEdit.text()
        if '?' not in url:
            url = url + '?'
        for i in get.split():
            url += i
            if i != get.split()[-1]:
                url += '&'
        data = {}
        for i in post.split():
            t = i.split('=')
            data[t[0]] = t[1]
        header = {}
        for i in head.split():
            t = i.split('=')
            header[t[0]] = t[1]
        res = requests.post(url, data, headers=header)
        res.encoding = 'utf-8'
        self.sourceShow.setPlainText(res.text)
        view = QWebEngineView(self.browView)
        view.setHtml(res.text)
        try:
            title = res.text.split('<title>')[1].split('</title>')[0]
            self.titleShow.setText(title)
        except Exception as e:
            self.titleShow.setText(url[:50])
        view.setFixedWidth(self.browView.width())
        view.setFixedHeight(self.browView.height())
        view.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWidget()
    myWin.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from gui import Ui_Form
import base64


def caesar(i, p):
    t = ord(i) + p
    if 'a' <= i <= 'z':
        if t > ord('z'):
            t -= 26
        if t < ord('a'):
            t += 26
    if 'A' <= i <= 'Z':
        if t > ord('Z'):
            t -= 26
        if t < ord('A'):
            t += 26
    return chr(t)



class MyWin(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        self.setupUi(self)

    def caesarBtnClicked(self):
        inp = self.inputEdit.toPlainText()
        out = []
        p = int(self.caeserEdit.text())
        for i in inp:
            if i.isalpha():
                out.append(caesar(i, p))
            else:
                out.append(i)
        self.resultEdit.setPlainText(''.join(out))

    def plusBtnClicked(self):
        self.caeserEdit.setText(str(int(self.caeserEdit.text()) + 1))

    def subBtnClicked(self):
        self.caeserEdit.setText(str(int(self.caeserEdit.text()) - 1))

    def b64en(self):
        inp = self.inputEdit.toPlainText().encode()
        self.resultEdit.setPlainText(base64.b64encode(inp).decode())

    def b64de(self):
        try:
            inp = self.inputEdit.toPlainText().encode()
            self.resultEdit.setPlainText(base64.b64decode(inp).decode())
        except Exception as e:
            self.resultEdit.setPlainText(str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWin()
    myWin.show()
    sys.exit(app.exec_())
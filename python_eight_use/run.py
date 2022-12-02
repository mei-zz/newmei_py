import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QDialog
from PyQt5 import QtCore

from main import Ui_Form

class MyWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    #适配2k等高分辨率屏幕
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.all_function()    # 执行选择函数功能
    myWin.show()
    sys.exit(app.exec_())

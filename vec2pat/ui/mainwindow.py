import sys
from PyQt4 import QtGui, QtCore
from vec2pat import *


class Window(QtGui.QMainWindow):
    # vc5 = VC5Get()
    vc5_search_path = '.'

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle("MMT J750 Pattern Generation Tool")
        self.setWindowIcon(QtGui.QIcon('IDTLogo.png'))
        # self.show()
        self.vc5_load_config()

    # def selectFile():
    #     lineEdit.setText(QFileDialog.getOpenFileName())
    #
    #     pushButton.clicked.connect(selectFile)

    def browse(self):
        filedialog = QtGui.QFileDialog(self)
        filedialog.show()
        filename = QtGui.QFileDialog.getOpenFileName()

    def vc5_load_config(self):
        btn = QtGui.QPushButton("Browse", self)
        # pushButton.clicked.connect(selectFile)

        QtCore.QObject.connect(btn, QtCore.SIGNAL('clicked()'), lambda: self.browse())
        # btn.clicked.connect(lambda: self.browse())
        # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(100, 100)
        self.show()

    def stop_app(self):
        print("Stop")
        self.setWindowTitle("@@@@@")


app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())

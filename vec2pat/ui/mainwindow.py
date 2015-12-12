import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle("MMT J750 Pattern Generation Tool")
        self.setWindowIcon(QtGui.QIcon('IDTlogo.png'))
        # self.show()
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        QtCore.QObject.connect(btn, QtCore.SIGNAL('clicked()'), quit())
        self.show()


app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())

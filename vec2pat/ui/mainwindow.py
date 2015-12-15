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

    def on_push_browse_btn(self):
        # filedialog = QtGui.QFileDialog(self)
        # filedialog.show()
        filename = QtGui.QFileDialog.getOpenFileName(
            self, "Open VersaClock Timing Commander Summary File", "C:\\", "Text files (*.txt);; All Files (*)")
        print(filename)
        return filename

    def vc5_load_config(self):
        btn = QtGui.QPushButton("Browse", self)
        QtCore.QObject.connect(btn, QtCore.SIGNAL('clicked()'), lambda: self.on_push_browse_btn())
        # btn.clicked.connect(lambda: self.browse())
        # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(100, 100)
        self.show()


def VC5initWindow():
    app = QtGui.QApplication(sys.argv)
    Window()
    sys.exit(app.exec_())

VC5initWindow()

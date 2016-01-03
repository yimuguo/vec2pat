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
        self.vc5_summary_browse_btn()
        self.vc5_directory_line()
        self.show()
    # def selectFile():
    #     lineEdit.setText(QFileDialog.getOpenFileName())
    #
    #     pushButton.clicked.connect(selectFile)

    def on_push_browse_btn(self):
        # filedialog = QtGui.QFileDialog(self)
        # filedialog.show()
        filename = QtGui.QFileDialog.getOpenFileName(
            self, "Open VersaClock Timing Commander Summary File",
            "C:\\",
            "Text files (*.txt);; All Files (*)")
        print(filename)
        return filename

    def vc5_summary_browse_btn(self):
        btn = QtGui.QPushButton("...", self)
        QtCore.QObject.connect(btn, QtCore.SIGNAL('clicked()'), lambda: self.on_push_browse_btn())
        # btn.clicked.connect(lambda: self.browse())
        # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(btn.minimumSizeHint())
        btn.move(100, 100)

    def vc5_directory_line(self):
        fileline = QtGui.QLineEdit("C:\\", self)
        fileline.resize(fileline.minimumSizeHint())
        fileline.setGeometry(10, 10, 50, 60)
        fileline.setAlignment(QtCore.Qt.AlignLeft)


def main():
    app = QtGui.QApplication(sys.argv)
    Window()
    sys.exit(app.exec_())

main()

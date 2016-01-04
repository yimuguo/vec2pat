from PyQt4 import QtGui
import sys
from vec2pat.ui import windowui
from vec2pat import vc5_summary
import os


class Window(QtGui.QMainWindow, windowui.Ui_MainWindow):
    # vc5_path = r"S:\Test_Eng\J750_HW_SW\VC5\AK652_008_802_Samsung\code"
    vc3_path = "S:\\Test_Eng\\J750_SW_HW\\VC5\\AK652_008_802_Samsung\\Code910"
    # vc5_filename = "S:\\Test_Eng\\J750_SW_HW\\VC5\\AK652_008_802_Samsung\\code\\"
    vc3_filename = r"S:\Test_Eng\J750_HW_SW\VC5\AK652_008_802_Samsung\Code910\OneConfigUpDown.txt"

    vc5_filename = r"E:\Documents\Github\vec2pat\vec2pat\tests\5P49V5901B-686_A#1_VCO_bits_Off_Summary.txt"
    vc5_path = r"E:\Documents\Github\vec2pat\vec2pat\tests"

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        self.vc5_path_file.setText(self.vc5_filename)
        self.vc3_path_file.setText(self.vc3_filename)
        self.vc5_btn_file.clicked.connect(lambda: self.brws_conf_btn('vc5'))
        self.vc5_btn_pat.clicked.connect(lambda: self.brws_dir_btn('vc5'))
        self.vc5_btn_workbook.clicked.connect(lambda: self.brws_conf_btn('vc5'))
        self.vc3_btn_file.clicked.connect(lambda: self.brws_conf_btn('vc3'))

    # def on_push_brws_btn(self, path, title_txt):
    #     #   This is the non-native dialog, speed problem with network drives
    #     dialog = QtGui.QFileDialog(self)
    #     dialog.setWindowTitle(title_txt)
    #     dialog.setDirectory(path)
    #     dialog.setNameFilter("Text files (*.txt);; All Files (*)")
    #     dialog.ReadOnly()
    #     dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
    #     if dialog.exec_() == QtGui.QDialog.Accepted:
    #         self.vc5_path = dialog.selectedFiles()[0]

    def brws_dir_btn(self, tab_type):
        if tab_type == 'vc5':
            self.vc5_path = QtGui.QFileDialog.getExistingDirectory(
                                self,
                                "Select Folder",
                                self.vc5_path
                                )
            print(self.vc5_filename)
            if self.vc5_filename is not '':
                self.vc5_path_file.setText(self.vc5_filename)
                path_break = self.vc5_filename.split('/')
                del path_break[-2]
                self.vc5_path = '/'.join(path_break)
                self.vc5_path_pat.setText(self.vc5_path + '')
            print(self.vc5_path)
        elif tab_type == 'vc3':
            self.vc3_filename = QtGui.QFileDialog.getExistingDirectory(
                                self,
                                "Select Folder",
                                self.vc3_path
                                )
            print(self.vc3_filename)
            if self.vc3_filename is not '':
                self.vc3_path_file.setText(self.vc3_filename)

    def brws_conf_btn(self, tab_type):
        if tab_type == 'vc5':
            self.vc5_filename = QtGui.QFileDialog.getOpenFileName(
                                self,
                                "Open VersaClock Timing Commander Summary File",
                                self.vc5_path,
                                "Text files (*.txt);; All Files (*)",
                                QtGui.QFileDialog.ReadOnly)
            print(self.vc5_filename)
            if self.vc5_filename is not '':
                self.vc5_path_file.setText(self.vc5_filename)
                vc5 = vc5_summary.VC5Get()
                vc5.summary_file = open(self.vc5_filename, 'r')
                if self.vco_mon.checkState() == 2:
                    vc5.vco_mon = False
                else:
                    vc5.vco_mon = True
                print(vc5.vco_mon)
                vc5.process_file()
                path_break = self.vc5_filename.split('/')
                path_break = path_break[0:-2]
                self.vc5_path = '/'.join(path_break)
                self.vc5_path_pat.setText(self.vc5_path + '/patterns' + vc5.i2c_address + '/')
                self.vc5_path_workbook.setText(self.vc5_path)
            print(self.vc5_path)
        elif tab_type == 'vc3':
            self.vc3_filename = QtGui.QFileDialog.getOpenFileName(
                                self,
                                "Open VersaClock4 Txt Configuration File",
                                self.vc3_path,
                                "Text files (*.txt);; All Files (*)",
                                QtGui.QFileDialog.ReadOnly)
            print(self.vc3_filename)
            if self.vc3_filename is not '':
                self.vc3_path_file.setText(self.vc3_filename)

    # def browse_folder(self):
    #     self.listWidget.clear() # In case there are any existing elements in the list
    #     directory = QtGui.QFileDialog.getExistingDirectory(self,
    #                                                        "Pick a folder")
    #     # execute getExistingDirectory dialog and set the directory variable to be equal
    #     # to the user selected directory
    #
    #     if directory: # if user didn't pick a directory don't continue
    #         for file_name in os.listdir(directory): # for all files, if any, in the directory
    #             self.listWidget.addItem(file_name)  # add file to the listWidget


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    pattool = Window()
    pattool.show()
    sys.exit(app.exec_())  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()                  # run the main function

main()

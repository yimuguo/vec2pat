from PyQt4 import QtGui
import sys
from vec2pat.ui import windowui
from vec2pat import vc5_summary
from vec2pat import reg2pat
import os
import glob


class Window(QtGui.QMainWindow, windowui.Ui_MainWindow):
    # vc5_path = r"S:\Test_Eng\J750_HW_SW\VC5\AK652_008_802_Samsung\code"
    # vc5_filename = r"S:/Test_Eng/J750_HW_SW/VC5/AK652_008_802_Samsung/code/5P49V5901-802_B#1_Summary.txt"
    vc3_path = "S:\\Test_Eng\\J750_SW_HW\\VC5\\AK652_008_802_Samsung\\Code910"
    vc3_filename = r"S:\Test_Eng\J750_HW_SW\VC5\AK652_008_802_Samsung\Code910\OneConfigUpDown.txt"

    vc5_filename = r"..\tests\code\5P49V5901B-686_A#1_VCO_bits_Off_Summary.txt"
    vc5_path = r"..\tests"

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # ======================VC5 Tab=====================================#
        self.vc5_path_file.setText(self.vc5_filename)
        self.vc5_btn_file.clicked.connect(lambda: self.brws_conf_btn('vc5'))
        self.vc5_btn_pat.clicked.connect(lambda: self.brws_dir_btn('vc5'))
        self.vc5_btn_workbook.clicked.connect(lambda: self.brws_conf_btn('vc5', 1))
        self.vc5_btn_gen.clicked.connect(lambda: self.gen_pat_btn_vc5())
        self.vc5_btn_compile.clicked.connect(lambda: self.compile_btn_vc5())
        # ======================VC3 Tab====================================
        self.vc3_path_file.setText(self.vc3_filename)
        self.vc3_btn_file.clicked.connect(lambda: self.brws_conf_btn('vc3'))

    def on_push_brws_btn(self, path, title_txt):
        #   This is the non-native dialog, speed problem with network drives
        dialog = QtGui.QFileDialog(self)
        dialog.setWindowTitle(title_txt)
        dialog.setDirectory(path)
        dialog.setNameFilter("Text files (*.txt);; All Files (*)")
        dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.vc5_filename = dialog.selectedFiles()[0]

    def compile_btn_vc5(self):
        for x in range(0, 4):
            if self.vc5.conf_enable[x] == 1:
                self.otp_wconfig = reg2pat.WritePat(self.vc5_path_pat.text() + '/OTP_wconfig%d.atp' % x, self.vc5.i2c_address)
                if self.atp_gen_vc5.checkState() == 2:
                    self.otp_wconfig.write_header('OTP_config%d' % x, 'SCLsel0', 'SDAsel1')
                    self.otp_wconfig.wbyte_lst(self.vc5.conf[x], 0, int('0x69', 0) + 1)
                    self.otp_wconfig.close_pat()
                self.otp_wconfig.compile_pat(self.vc5_path)
                # Write Reading Register Patterns
                self.otp_rconfig = reg2pat.WritePat(self.vc5_path_pat.text() + 'OTP_rconfig%d.atp' % x, self.vc5.i2c_address)
                if self.atp_gen_vc5.checkState() == 2:
                    self.otp_rconfig.write_header('OTP_config%d' % x, 'SCLsel0', 'SDAsel1')
                    self.otp_rconfig.rbyte_lst(self.vc5.conf[x], 0, int('0x69', 0) + 1)
                    self.otp_rconfig.close_pat()
                self.otp_rconfig.compile_pat(self.vc5_path)
                if self.del_atp_vc5.checkState() == 2:
                    os.remove(os.path.join(self.vc5_path_pat.text(), "OTP_wconfig%d.LOG" % x))
                    os.remove(os.path.join(self.vc5_path_pat.text(), "OTP_wconfig%d.atp" % x))
                    os.remove(os.path.join(self.vc5_path_pat.text(), "OTP_rconfig%d.LOG" % x))
                    os.remove(os.path.join(self.vc5_path_pat.text(), "OTP_rconfig%d.atp" % x))

    def brws_conf_btn(self, tab_type, btn_type=0):
        if tab_type == 'vc5':
            if btn_type != 1:
                # self.on_push_brws_btn("S:\\Test_Eng\\J750_HW_SW\\VC5\\AK652_008_802_Samsung\\",
                #                       "Open VersaClock Timing Commander Summary File")

                self.vc5_filename = QtGui.QFileDialog.getOpenFileName(
                                    self,
                                    "Open VersaClock Timing Commander Summary File",
                                    self.vc5_path_file.text(),   # Need to break the current input box into path
                                    "Text files (*.txt);; All Files (*)",
                                    QtGui.QFileDialog.ReadOnly)
                print(self.vc5_filename)
                if self.vc5_filename is not '':
                    self.vc5_path_file.setText(self.vc5_filename)
                    self.vc5 = vc5_summary.VC5Get()
                    self.vc5.summary_file = open(self.vc5_filename, 'r')
                    if self.vco_mon_off.checkState() == 2:
                        self.vc5.vco_mon = False
                    else:
                        self.vc5.vco_mon = True
                    print(self.vc5.vco_mon)
                    self.vc5.process_file()
                    path_break = self.vc5_filename.split('/')
                    path_break = path_break[0:-2]
                    self.vc5_path = "/".join(path_break)
                    self.vc5_path_pat.setText(self.vc5_path + '/patterns' + self.vc5.i2c_address + '/patsmb/')
                    for workbook in glob.glob(os.path.join(self.vc5_path, "*FT*.xls")):
                        self.vc5_path_workbook.setText(workbook)
            else:
                workbook_filename = QtGui.QFileDialog.getOpenFileName(
                                    self,
                                    "Select IG-XL Workbook",
                                    self.vc5_path_workbook.text(),   # Need to break the current input box into path
                                    "IG-XL Workbook (*.xls; *.xlsx);; Text files (*.txt);; All Files (*)",
                                    QtGui.QFileDialog.ReadOnly)
                if workbook_filename is not '':
                    self.vc5_path_workbook.setText(workbook_filename)
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

    def gen_pat_btn_vc5(self):
        for x in range(0, 4):
            if self.vc5.conf_enable[x] == 1:
                self.otp_wconfig = reg2pat.WritePat(self.vc5_path_pat.text() + '/OTP_wconfig%d.atp' % x, self.vc5.i2c_address)
                self.otp_wconfig.write_header('OTP_config%d' % x, 'SCLsel0', 'SDAsel1')
                self.otp_wconfig.wbyte_lst(self.vc5.conf[x], 0, int('0x69', 0) + 1)
                self.otp_wconfig.close_pat()
                # Write Reading Register Patterns
                self.otp_rconfig = reg2pat.WritePat(self.vc5_path_pat.text() + 'OTP_rconfig%d.atp' % x, self.vc5.i2c_address)
                self.otp_rconfig.write_header('OTP_config%d' % x, 'SCLsel0', 'SDAsel1')
                self.otp_rconfig.rbyte_lst(self.vc5.conf[x], 0, int('0x69', 0) + 1)
                self.otp_rconfig.close_pat()

    def brws_dir_btn(self, tab_type):
        if tab_type == 'vc5':
            pat_path = QtGui.QFileDialog.getExistingDirectory(
                                self,
                                "Select Folder",
                                self.vc5_path_pat.text()
                                )
            if pat_path is not '':
                self.vc5_path_pat.setText(pat_path)
        elif tab_type == 'vc3':
            self.vc3_filename = QtGui.QFileDialog.getExistingDirectory(
                                self,
                                "Select Folder",
                                self.vc3_path_pat.text()
                                )
            print(self.vc3_filename)
            if self.vc3_filename is not '':
                self.vc3_path_file.setText(self.vc3_filename)


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    pattool = Window()
    pattool.show()
    sys.exit(app.exec_())  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()                  # run the main function

main()

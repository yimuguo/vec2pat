# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(576, 375)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.general = QtGui.QWidget()
        self.general.setObjectName(_fromUtf8("general"))
        self.pat_input = QtGui.QTextEdit(self.general)
        self.pat_input.setGeometry(QtCore.QRect(20, 10, 341, 121))
        self.pat_input.setObjectName(_fromUtf8("pat_input"))
        self.btn_gen = QtGui.QPushButton(self.general)
        self.btn_gen.setGeometry(QtCore.QRect(420, 140, 101, 41))
        self.btn_gen.setObjectName(_fromUtf8("btn_gen"))
        self.btn_compile = QtGui.QPushButton(self.general)
        self.btn_compile.setGeometry(QtCore.QRect(420, 210, 101, 41))
        self.btn_compile.setObjectName(_fromUtf8("btn_compile"))
        self.btn_workbook = QtGui.QPushButton(self.general)
        self.btn_workbook.setGeometry(QtCore.QRect(370, 230, 41, 21))
        self.btn_workbook.setObjectName(_fromUtf8("btn_workbook"))
        self.del_atp = QtGui.QCheckBox(self.general)
        self.del_atp.setGeometry(QtCore.QRect(380, 290, 131, 16))
        self.del_atp.setChecked(True)
        self.del_atp.setObjectName(_fromUtf8("del_atp"))
        self.path_workbook = QtGui.QLineEdit(self.general)
        self.path_workbook.setGeometry(QtCore.QRect(20, 230, 341, 21))
        self.path_workbook.setObjectName(_fromUtf8("path_workbook"))
        self.btn_pat = QtGui.QPushButton(self.general)
        self.btn_pat.setGeometry(QtCore.QRect(370, 160, 41, 21))
        self.btn_pat.setObjectName(_fromUtf8("btn_pat"))
        self.path_pat = QtGui.QLineEdit(self.general)
        self.path_pat.setGeometry(QtCore.QRect(20, 160, 341, 21))
        self.path_pat.setObjectName(_fromUtf8("path_pat"))
        self.i2c_add = QtGui.QComboBox(self.general)
        self.i2c_add.setGeometry(QtCore.QRect(380, 30, 41, 21))
        self.i2c_add.setEditable(True)
        self.i2c_add.setObjectName(_fromUtf8("i2c_add"))
        self.i2c_add.addItem(_fromUtf8(""))
        self.i2c_add.addItem(_fromUtf8(""))
        self.i2c_add.addItem(_fromUtf8(""))
        self.scl = QtGui.QLineEdit(self.general)
        self.scl.setGeometry(QtCore.QRect(480, 30, 51, 20))
        self.scl.setAlignment(QtCore.Qt.AlignCenter)
        self.scl.setObjectName(_fromUtf8("scl"))
        self.sda = QtGui.QLineEdit(self.general)
        self.sda.setGeometry(QtCore.QRect(480, 70, 51, 20))
        self.sda.setAlignment(QtCore.Qt.AlignCenter)
        self.sda.setObjectName(_fromUtf8("sda"))
        self.label_7 = QtGui.QLabel(self.general)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 341, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.general)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 341, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.general)
        self.label_9.setGeometry(QtCore.QRect(480, 10, 41, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.general)
        self.label_10.setGeometry(QtCore.QRect(480, 50, 71, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.general)
        self.label_11.setGeometry(QtCore.QRect(380, 10, 41, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.numofpat = QtGui.QComboBox(self.general)
        self.numofpat.setGeometry(QtCore.QRect(500, 110, 31, 22))
        self.numofpat.setEditable(True)
        self.numofpat.setObjectName(_fromUtf8("numofpat"))
        self.numofpat.addItem(_fromUtf8(""))
        self.numofpat.addItem(_fromUtf8(""))
        self.numofpat.addItem(_fromUtf8(""))
        self.numofpat.addItem(_fromUtf8(""))
        self.label_12 = QtGui.QLabel(self.general)
        self.label_12.setGeometry(QtCore.QRect(480, 90, 61, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.atp_gen = QtGui.QCheckBox(self.general)
        self.atp_gen.setGeometry(QtCore.QRect(380, 270, 131, 16))
        self.atp_gen.setChecked(True)
        self.atp_gen.setObjectName(_fromUtf8("atp_gen"))
        self.pat_name = QtGui.QLineEdit(self.general)
        self.pat_name.setGeometry(QtCore.QRect(380, 110, 101, 21))
        self.pat_name.setObjectName(_fromUtf8("pat_name"))
        self.label_13 = QtGui.QLabel(self.general)
        self.label_13.setGeometry(QtCore.QRect(380, 90, 71, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.offset = QtGui.QLineEdit(self.general)
        self.offset.setGeometry(QtCore.QRect(380, 70, 31, 20))
        self.offset.setAlignment(QtCore.Qt.AlignCenter)
        self.offset.setObjectName(_fromUtf8("offset"))
        self.label_14 = QtGui.QLabel(self.general)
        self.label_14.setGeometry(QtCore.QRect(380, 50, 71, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.tabWidget.addTab(self.general, _fromUtf8(""))
        self.vc5_tab = QtGui.QWidget()
        self.vc5_tab.setObjectName(_fromUtf8("vc5_tab"))
        self.vc5_path_file = QtGui.QLineEdit(self.vc5_tab)
        self.vc5_path_file.setGeometry(QtCore.QRect(20, 30, 341, 21))
        self.vc5_path_file.setObjectName(_fromUtf8("vc5_path_file"))
        self.vc5_btn_file = QtGui.QPushButton(self.vc5_tab)
        self.vc5_btn_file.setGeometry(QtCore.QRect(370, 30, 41, 21))
        self.vc5_btn_file.setObjectName(_fromUtf8("vc5_btn_file"))
        self.vco_mon_off = QtGui.QCheckBox(self.vc5_tab)
        self.vco_mon_off.setGeometry(QtCore.QRect(420, 30, 111, 17))
        self.vco_mon_off.setChecked(True)
        self.vco_mon_off.setObjectName(_fromUtf8("vco_mon_off"))
        self.vc5_btn_compile = QtGui.QPushButton(self.vc5_tab)
        self.vc5_btn_compile.setGeometry(QtCore.QRect(420, 170, 101, 41))
        self.vc5_btn_compile.setObjectName(_fromUtf8("vc5_btn_compile"))
        self.vc5_btn_workbook = QtGui.QPushButton(self.vc5_tab)
        self.vc5_btn_workbook.setGeometry(QtCore.QRect(370, 190, 41, 21))
        self.vc5_btn_workbook.setObjectName(_fromUtf8("vc5_btn_workbook"))
        self.del_atp_vc5 = QtGui.QCheckBox(self.vc5_tab)
        self.del_atp_vc5.setGeometry(QtCore.QRect(380, 240, 131, 16))
        self.del_atp_vc5.setChecked(True)
        self.del_atp_vc5.setObjectName(_fromUtf8("del_atp_vc5"))
        self.vc5_path_workbook = QtGui.QLineEdit(self.vc5_tab)
        self.vc5_path_workbook.setGeometry(QtCore.QRect(20, 190, 341, 21))
        self.vc5_path_workbook.setObjectName(_fromUtf8("vc5_path_workbook"))
        self.vc5_btn_gen = QtGui.QPushButton(self.vc5_tab)
        self.vc5_btn_gen.setGeometry(QtCore.QRect(420, 60, 101, 41))
        self.vc5_btn_gen.setObjectName(_fromUtf8("vc5_btn_gen"))
        self.vc5_btn_pat = QtGui.QPushButton(self.vc5_tab)
        self.vc5_btn_pat.setGeometry(QtCore.QRect(370, 80, 41, 21))
        self.vc5_btn_pat.setObjectName(_fromUtf8("vc5_btn_pat"))
        self.vc5_path_pat = QtGui.QLineEdit(self.vc5_tab)
        self.vc5_path_pat.setGeometry(QtCore.QRect(20, 80, 341, 21))
        self.vc5_path_pat.setObjectName(_fromUtf8("vc5_path_pat"))
        self.label = QtGui.QLabel(self.vc5_tab)
        self.label.setGeometry(QtCore.QRect(20, 10, 341, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.vc5_tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 341, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.vc5_tab)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 341, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.atp_gen_vc5 = QtGui.QCheckBox(self.vc5_tab)
        self.atp_gen_vc5.setGeometry(QtCore.QRect(380, 220, 131, 16))
        self.atp_gen_vc5.setChecked(True)
        self.atp_gen_vc5.setObjectName(_fromUtf8("atp_gen_vc5"))
        self.tabWidget.addTab(self.vc5_tab, _fromUtf8(""))
        self.vc3_tab = QtGui.QWidget()
        self.vc3_tab.setObjectName(_fromUtf8("vc3_tab"))
        self.vc3_btn_file = QtGui.QPushButton(self.vc3_tab)
        self.vc3_btn_file.setGeometry(QtCore.QRect(370, 30, 41, 21))
        self.vc3_btn_file.setObjectName(_fromUtf8("vc3_btn_file"))
        self.vc3_path_file = QtGui.QLineEdit(self.vc3_tab)
        self.vc3_path_file.setGeometry(QtCore.QRect(20, 30, 341, 21))
        self.vc3_path_file.setObjectName(_fromUtf8("vc3_path_file"))
        self.vc3_btn_gen = QtGui.QPushButton(self.vc3_tab)
        self.vc3_btn_gen.setGeometry(QtCore.QRect(420, 60, 101, 41))
        self.vc3_btn_gen.setObjectName(_fromUtf8("vc3_btn_gen"))
        self.vc3_btn_compile = QtGui.QPushButton(self.vc3_tab)
        self.vc3_btn_compile.setGeometry(QtCore.QRect(420, 170, 101, 41))
        self.vc3_btn_compile.setObjectName(_fromUtf8("vc3_btn_compile"))
        self.vc3_btn_workbook = QtGui.QPushButton(self.vc3_tab)
        self.vc3_btn_workbook.setGeometry(QtCore.QRect(370, 190, 41, 21))
        self.vc3_btn_workbook.setObjectName(_fromUtf8("vc3_btn_workbook"))
        self.del_atp_vc3 = QtGui.QCheckBox(self.vc3_tab)
        self.del_atp_vc3.setGeometry(QtCore.QRect(380, 240, 131, 16))
        self.del_atp_vc3.setChecked(True)
        self.del_atp_vc3.setObjectName(_fromUtf8("del_atp_vc3"))
        self.vc3_path_workbook = QtGui.QLineEdit(self.vc3_tab)
        self.vc3_path_workbook.setGeometry(QtCore.QRect(20, 190, 341, 21))
        self.vc3_path_workbook.setObjectName(_fromUtf8("vc3_path_workbook"))
        self.vc3_btn_pat = QtGui.QPushButton(self.vc3_tab)
        self.vc3_btn_pat.setGeometry(QtCore.QRect(370, 80, 41, 21))
        self.vc3_btn_pat.setObjectName(_fromUtf8("vc3_btn_pat"))
        self.vc3_path_pat = QtGui.QLineEdit(self.vc3_tab)
        self.vc3_path_pat.setGeometry(QtCore.QRect(20, 80, 341, 21))
        self.vc3_path_pat.setObjectName(_fromUtf8("vc3_path_pat"))
        self.label_4 = QtGui.QLabel(self.vc3_tab)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 341, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.vc3_tab)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 341, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.vc3_tab)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 341, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.atp_gen_vc3 = QtGui.QCheckBox(self.vc3_tab)
        self.atp_gen_vc3.setGeometry(QtCore.QRect(380, 220, 131, 16))
        self.atp_gen_vc3.setChecked(True)
        self.atp_gen_vc3.setObjectName(_fromUtf8("atp_gen_vc3"))
        self.tabWidget.addTab(self.vc3_tab, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.vc5_path_file, self.vc5_btn_file)
        MainWindow.setTabOrder(self.vc5_btn_file, self.vco_mon_off)
        MainWindow.setTabOrder(self.vco_mon_off, self.del_atp)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MMT J750 400Khz I2C Pattern Tool", None))
        self.btn_gen.setText(_translate("MainWindow", "Generate Pattern", None))
        self.btn_compile.setText(_translate("MainWindow", "Compile Pattern", None))
        self.btn_workbook.setText(_translate("MainWindow", "...", None))
        self.del_atp.setText(_translate("MainWindow", "Del *.atp Source Vector", None))
        self.btn_pat.setText(_translate("MainWindow", "...", None))
        self.i2c_add.setItemText(0, _translate("MainWindow", "D0", None))
        self.i2c_add.setItemText(1, _translate("MainWindow", "D2", None))
        self.i2c_add.setItemText(2, _translate("MainWindow", "D4", None))
        self.scl.setText(_translate("MainWindow", "SCL", None))
        self.sda.setText(_translate("MainWindow", "SDA", None))
        self.label_7.setText(_translate("MainWindow", "Generate Pattern to Path:", None))
        self.label_8.setText(_translate("MainWindow", "Compile Against IG-XL Workbook:", None))
        self.label_9.setText(_translate("MainWindow", "SCL Pin", None))
        self.label_10.setText(_translate("MainWindow", "SDA Pinname", None))
        self.label_11.setText(_translate("MainWindow", "I2C Addr", None))
        self.numofpat.setItemText(0, _translate("MainWindow", "1", None))
        self.numofpat.setItemText(1, _translate("MainWindow", "2", None))
        self.numofpat.setItemText(2, _translate("MainWindow", "3", None))
        self.numofpat.setItemText(3, _translate("MainWindow", "4", None))
        self.label_12.setText(_translate("MainWindow", "# of Pat", None))
        self.atp_gen.setText(_translate("MainWindow", "Auto-generate atp fiels", None))
        self.label_13.setText(_translate("MainWindow", "Pattern Name:", None))
        self.offset.setText(_translate("MainWindow", "0", None))
        self.label_14.setText(_translate("MainWindow", "Start Offset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general), _translate("MainWindow", "General Purpose", None))
        self.vc5_btn_file.setText(_translate("MainWindow", "...", None))
        self.vco_mon_off.setText(_translate("MainWindow", "VCO Monitor OFF", None))
        self.vc5_btn_compile.setText(_translate("MainWindow", "Compile Pattern", None))
        self.vc5_btn_workbook.setText(_translate("MainWindow", "...", None))
        self.del_atp_vc5.setText(_translate("MainWindow", "Del *.atp Source Vector", None))
        self.vc5_btn_gen.setText(_translate("MainWindow", "Generate Pattern", None))
        self.vc5_btn_pat.setText(_translate("MainWindow", "...", None))
        self.label.setText(_translate("MainWindow", "Timing Commander Summary File:", None))
        self.label_2.setText(_translate("MainWindow", "Generate Pattern to Path:", None))
        self.label_3.setText(_translate("MainWindow", "Compile Against IG-XL Workbook:", None))
        self.atp_gen_vc5.setText(_translate("MainWindow", "Auto-generate atp fiels", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vc5_tab), _translate("MainWindow", "VersaClock 5", None))
        self.vc3_btn_file.setText(_translate("MainWindow", "...", None))
        self.vc3_btn_gen.setText(_translate("MainWindow", "Generate Pattern", None))
        self.vc3_btn_compile.setText(_translate("MainWindow", "Compile Pattern", None))
        self.vc3_btn_workbook.setText(_translate("MainWindow", "...", None))
        self.del_atp_vc3.setText(_translate("MainWindow", "Del *.atp Source Vector", None))
        self.vc3_btn_pat.setText(_translate("MainWindow", "...", None))
        self.label_4.setText(_translate("MainWindow", "Generate Pattern to Path:", None))
        self.label_5.setText(_translate("MainWindow", "VersaClock 3 Configuration File:", None))
        self.label_6.setText(_translate("MainWindow", "Compile Against IG-XL Workbook:", None))
        self.atp_gen_vc3.setText(_translate("MainWindow", "Auto-generate atp fiels", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vc3_tab), _translate("MainWindow", "VersaClock 3", None))


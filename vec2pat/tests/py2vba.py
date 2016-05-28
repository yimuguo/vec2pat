import win32com.client as win32
import os


class py2vba(object):
    i2c_add = "D0"
    conf_en = [1, 0, 0, 0]
    ref = [25, 25, 25, 25]
    fout = [[133.33333, 133.33333, 100, 100], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    tout = [['LPHCSL', 'LPHCSL', 'LPHCSL', 'LPHCSL']]
    sout = [[0, 0, 0, 0]]
    src_str = "Public Sub UpdateConfig()\n"

    def __init__(self, wbfile):
        self.wbfile = wbfile
        self.xl = win32.DispatchEx('Excel.Application')
        self.xl.Visible = False
        self.workbook = self.xl.Workbooks.Open(self.wbfile)

    def add_func(self):
        xlmodule = self.workbook.VBProject.VBComponents.Add(1)
        xlmodule.CodeModule.AddFromString(self.src_str)

    def update_config(self):
        for cfgnum in range(0, 4):
            self.src_str += "Config_en(" + str(cfgnum) + ") = " + str(self.conf_en[cfgnum]) + '\n'
            if self.conf_en[cfgnum] == 1:
                self.src_str += "\n"
                self.src_str += "Fout0(" + str(cfgnum) + ")" + " = " + str(self.ref[cfgnum]) + '\n'
                self.src_str += "\nREFclk(" + str(cfgnum) + ") = Fout0(" + str(cfgnum) + ")" + '\n'
                self.src_str += "Fout1(" + str(cfgnum) + ") = " + str(self.fout[cfgnum][0]) + '\n'
                self.src_str += "Fout2(" + str(cfgnum) + ") = " + str(self.fout[cfgnum][1]) + '\n'
                self.src_str += "Fout3(" + str(cfgnum) + ") = " + str(self.fout[cfgnum][2]) + '\n'
                self.src_str += "Fout4(" + str(cfgnum) + ") = " + str(self.fout[cfgnum][3]) + '\n'
                self.src_str += "Sout1(" + str(cfgnum) + ") = " + str(self.sout[cfgnum][0]) + '\n'
                self.src_str += "Sout2(" + str(cfgnum) + ") = " + str(self.sout[cfgnum][1]) + '\n'
                self.src_str += "Sout3(" + str(cfgnum) + ") = " + str(self.sout[cfgnum][2]) + '\n'
                self.src_str += "Sout4(" + str(cfgnum) + ") = " + str(self.sout[cfgnum][3]) + '\n'
                self.src_str += "OPTout0(" + str(cfgnum) + ") = CMOS\n"
                self.src_str += "OPTout1(" + str(cfgnum) + ") = " + str(self.tout[cfgnum][0]) + '\n'
                self.src_str += "OPTout2(" + str(cfgnum) + ") = " + str(self.tout[cfgnum][1]) + '\n'
                self.src_str += "OPTout3(" + str(cfgnum) + ") = " + str(self.tout[cfgnum][2]) + '\n'
                self.src_str += "OPTout4(" + str(cfgnum) + ") = " + str(self.tout[cfgnum][3]) + '\n'
                self.src_str += "Prim_clock(" + str(cfgnum) + ") = " + str
        self.src_str += '''
For i = 0 To 3
    If Sout1(i) < 0 Then Fout1(i) = Fout1(i) + Fout1(i) * Sout1(i) / 100 / 2
    If Sout2(i) < 0 Then Fout2(i) = Fout2(i) + Fout2(i) * Sout2(i) / 100 / 2
    If Sout3(i) < 0 Then Fout3(i) = Fout3(i) + Fout3(i) * Sout3(i) / 100 / 2
    If Sout4(i) < 0 Then Fout4(i) = Fout4(i) + Fout4(i) * Sout4(i) / 100 / 2
Next i

For i = 0 To 3
    If Sout1(i) < 0 And Fout1b(i) <> 0 Then Fout1b(i) = Fout1b(i) + Fout1b(i) * Sout1(i) / 100 / 2
    If Sout2(i) < 0 And Fout2b(i) <> 0 Then Fout2b(i) = Fout2b(i) + Fout2b(i) * Sout2(i) / 100 / 2
    If Sout3(i) < 0 And Fout3b(i) <> 0 Then Fout3b(i) = Fout3b(i) + Fout3b(i) * Sout3(i) / 100 / 2
    If Sout4(i) < 0 And Fout4b(i) <> 0 Then Fout4b(i) = Fout4b(i) + Fout4b(i) * Sout4(i) / 100 / 2
Next i
end sub
        '''

    def close_wb(self):
        self.workbook.Close(True, currpath + "\\test.xls")
        self.xl.Quit()

currpath = os.getcwd()
testwb = py2vba(currpath + "\\5P49V5901B_FT_802_25C_rev0.xls")
testwb.update_config()
testwb.add_func()
testwb.close_wb()

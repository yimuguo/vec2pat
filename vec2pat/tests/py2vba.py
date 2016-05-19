import win32com.client as win32
import os


class py2vba(object):
    i2c_add = "D0"
    conf_en = [1, 0, 0, 0]
    fout = [[133.33333, 133.33333, 100, 100], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    tout = ['LPHCSL', 'LPHCSL', ]
    sout = [[]]

    def __init__(self, wbfile):
        self.wbfile = wbfile
        self.workbook = self.open_wb()

    def open_wb(self):
        xl = win32.gencache.EnsureDispatch('Excel.Application')
        xl.Visible = False
        workbook = xl.Workbooks.Open(self.wbfile)
        return workbook

    def add_func(self, src_str):
        xlmodule = self.workbook.VBProject.VBComponents.Add(1)
        xlmodule.CodeModule.AddFromString(src_str)

    def update_config(self, conf_en, fout, sout):
        scode = "Public Sub UpdateConfig()\n"

        for n in range(0, 4):
            scode += "Config_en(" + n + ") = " + conf_en[n]
            scode += "\n"
            scode += "\nREFclk(" + n + ") = Fout0(" + n + ")"

        sCode = '''
        Public Sub UpdateConfig()
        I2C_add = "%s"
        Config_en(0) = %d
        Config_en(1) = %d
        Config_en(2) = %d
        Config_en(3) = %d
        Fout0(0) = %d
        Fout0(1) = %d
        Fout0(2) = %d
        Fout0(3) = %d

        REFclk(0) = Fout0(0)
        REFclk(1) = Fout0(1)
        REFclk(2) = Fout0(2)
        REFclk(2) = Fout0(3)

        Fout1(0) = %d
        Fout2(0) = %d
        Fout3(0) = %d
        Fout4(0) = %d
        Sout1(0) = %d
        Sout2(0) = %d
        Sout3(0) = %d
        Sout4(0) = %d
        Fout1b(0) = %d
        Fout2b(0) = %d
        Fout3b(0) = %d
        Fout4b(0) = %d

        Fout1(1) = %d
        Fout2(1) = %d
        Fout3(1) = %d
        Fout4(1) = %d
        Sout1(1) = %d
        Sout2(1) = %d
        Sout3(1) = %d
        Sout4(1) = %d
        Fout1b(1) = %d
        Fout2b(1) = %d
        Fout3b(1) = %d
        Fout4b(1) = %d

        Fout1(2) = %d
        Fout2(2) = %d
        Fout3(2) = %d
        Fout4(2) = %d
        Sout1(2) = %d
        Sout2(2) = %d
        Sout3(2) = %d
        Sout4(2) = %d
        Fout1b(2) = %d
        Fout2b(2) = %d
        Fout3b(2) = %d
        Fout4b(2) = %d

        Fout1(3) = %d
        Fout2(3) = %d
        Fout3(3) = %d
        Fout4(3) = %d
        Sout1(3) = %d
        Sout2(3) = %d
        Sout3(3) = %d
        Sout4(3) = %d
        Fout1b(3) = %d
        Fout2b(3) = %d
        Fout3b(3) = %d
        Fout4b(3) = %d

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
        ''' % ()

    def close_wb(self):
        self.workbook.Close(True, currpath + "\\test.xls")

currpath = os.getcwd()
wbfile + "\\5P49V5901B_FT_802_25C_rev0.xls"

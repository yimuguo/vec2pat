import win32com.client as win32
import os

xl = win32.gencache.EnsureDispatch('Excel.Application')
xl.Visible = False
currpath = os.getcwd()
workbook = xl.Workbooks.Open(currpath + "\\5P49V5901B_FT_802_25C_rev0.xls")
xlmodule = workbook.VBProject.VBComponents.Add(1)
conf = 1

sCode = '''
Public Sub UpdateConfig
Config_en(0) = %d




end sub
''' % conf

xlmodule.CodeModule.AddFromString(sCode)
workbook.Close(True, currpath + "\\test.xls")

import win32com.client as win32

import comtypes, comtypes.client

xl = win32.gencache.EnsureDispatch('Excel.Application')
xl.Visible = True
ss = xl.Workbooks.Open(r"C:\Users\yguo\Documents\GitHub\vec2pat\vec2pat\tests\5P49V5901B_FT_802_25C_rev0.xls")
sh = ss.ActiveSheet

xlmodule = ss.VBProject.VBComponents.Add(1)  # vbext_ct_StdModule

sCode = '''sub VBAMacro()
       msgbox "VBA Macro called"
      end sub'''

xlmodule.CodeModule.AddFromString(sCode)
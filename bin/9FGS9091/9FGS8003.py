from vec2pat import *
__author__ = 'yguo'
VC3_FLAG = 'N'
VC3_LOG_DEL_FLAG = 'N'
I2C_ADD = 'D0'
os.chdir("S:\Test_Eng\J750_HW_SW\9FGSxxxx\patterns\\9FGS8003\\%s" % I2C_ADD)


strCFG0 = '80 43 0B 18 14 0B 18 14 0B 18 14 8B 18 14 8E 8E 83 1A 0C 80 00 02 96 00 00 00 A0 FC AF 00 0A 30 18 18 00 00 21 65'
print(str(len(strCFG0)))
config0 = strCFG0.split()
config0[26] = 'C0'
config0[27] = 'FC'
config0[27] = int(config0[27], 16) & 0b11110111
wbytes_pat(config0, 'writeCFG0', I2C_ADD)
rbytes_pat(config0, 'readCFG0', I2C_ADD, False, 26)

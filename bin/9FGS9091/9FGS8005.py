from vec2pat import *
__author__ = 'yguo'
VC3_FLAG = 'N'
VC3_LOG_DEL_FLAG = 'N'
I2C_ADD = 'D0'
os.chdir("S:\Test_Eng\J750_HW_SW\9FGSxxxx\patterns\\9FGS8005\\%s" % I2C_ADD)


strCFG0 = '80 0F 0F 11 34 0F 11 34 0F 11 34 BF 11 34 92 92 00 00 00 00 00 00 00 00 00 00 ED F4 CF 00 0F 21 00 10 00 00 21 65'
config0 = strCFG0.split()
config0[26] = 'C0'
config0[27] = 'FC'
config0[27] = int(config0[27], 16) & 0b11110111
config0[14] = 0x80
config0[15] = 0x80
wbytes_pat(config0, 'writeCFG0', I2C_ADD)
rbytes_pat(config0, 'readCFG0', I2C_ADD, False, 26)

strCFG1 = '80 0F 0F 11 34 0F 11 34 0F 11 34 BF 11 34 92 92 00 00 00 00 00 00 00 00 00 00 ED F4 CF 00 0F 20 00 10 00 00 21 65'
config1 = strCFG1.split()
config1[14] = 0x80
config1[15] = 0x80
config1[26] = 'C0'
config1[27] = 'FC'
config1[27] = int(config1[27], 16) & 0b11110111
wbytes_pat(config1, 'writeCFG1', I2C_ADD)
rbytes_pat(config1, 'readCFG1', I2C_ADD, False, 26)

htolStr = '80 4F BF 11 34 8E 12 14 BF 11 34 BF 11 34 94 94 83 1A 0C 80 00 02 96 00 00 00 D3 FC CF 00 0F 25 12 08 00 FF 21 65'
htol = htolStr.split()
htol[26] = 'C0'
htol[27] = 'FC'
htol[27] = int(htol[27], 16) & 0b11110111
wbytes_pat(htol, "HTOL_Write", I2C_ADD)
rbytes_pat(htol, "HTOL_Read", I2C_ADD, False, 26)

esdLU =   '80 0F 0F 11 34 0F 11 34 0F 11 34 0F 11 34 92 92 00 00 00 00 00 00 00 00 00 00 ED F4 CF 00 0F 21 00 10 00 00 21 65'
esdLU = esdLU.split()
esdLU[26] = 'A0'
esdLU[27] = 'FC'
# esdLU[27] = int(esdLU[27], 16) & 0b11110111
wbytes_pat(esdLU, "ESDLU_Write", I2C_ADD)
rbytes_pat(esdLU, "ESDLU_Read", I2C_ADD, True)

esdTest = '80 4F 0F 11 34 BF 11 34 0F 11 34 BF 11 34 92 92 00 00 00 00 00 00 00 00 00 00 ED F4 CF 00 0F 21 00 10 00 00 21 65'
esdTest = esdTest.split()
esdTest[26] = 'A0'
esdTest[27] = 'FC'
# esdTest[27] = int(esdTest[27], 16) & 0b11110111
wbytes_pat(esdTest, "ESDtest", I2C_ADD)

from vec2pat import *
__author__ = 'yguo'
VC3_FLAG = 'N'
VC3_LOG_DEL_FLAG = 'N'
I2C_ADD = 'D0'
os.chdir("S:\Test_Eng\J750_HW_SW\9FGSxxxx\\archive_docs_prgs\9FGS9091\AK692_008\patterns\%s" % I2C_ADD)

cfg0Str = '80 4F 8E 12 14 8E 12 14 8E 12 14 8E 12 14 80 80 83 1A 0C 80 00 02 96 00 00 00 A0 FC AF 00 0A 24 12 18 00 00 21 65'
cfg0 = re.split('\s+', cfg0Str)
cfg0[26] = 'C0'
cfg0[27] = int(cfg0[27], 16) & 0b11110111
wbytes_pat(cfg0, 'writeCFG0', I2C_ADD)
rbytes_pat(cfg0, 'readCFG0', I2C_ADD, False, 26)

cfg1Str = '80 4F 8E 12 14 8E 12 14 8E 12 14 8E 12 14 80 80 83 1A 0C 80 00 02 96 00 00 00 A0 FC AF 00 0A 24 12 19 00 00 21 65'
cfg1 = re.split('\s+', cfg1Str)
cfg1[26] = 'C0'
cfg1[27] = int(cfg1[27], 16) & 0b11110111
wbytes_pat(cfg1, 'writeCFG1', I2C_ADD)
rbytes_pat(cfg1, 'readCFG1', I2C_ADD, False, 26)

cfg2Str = '80 4F 8E 12 14 8E 12 14 8E 12 14 8E 12 14 80 80 83 1A 0C 80 00 02 96 00 00 00 A0 FC AF 00 0A 24 12 1A 00 00 21 65'
cfg2 = re.split('\s+', cfg2Str)
cfg2[26] = 'C0'
cfg2[27] = int(cfg2[27], 16) & 0b11110111
wbytes_pat(cfg2, 'writeCFG2', I2C_ADD)
rbytes_pat(cfg2, 'readCFG2', I2C_ADD, False, 26)

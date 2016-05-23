from vec2pat import *
__author__ = 'yguo'
VC3_FLAG = 'N'
VC3_LOG_DEL_FLAG = 'N'
I2C_ADD = 'D6'
os.chdir("S:\Test_Eng\J750_HW_SW\9FGSxxxx\9FGS9092\\patterns\%s" % I2C_ADD)


OutputsHiz_hex = ['E0', '5F', '8F', '61', '44', '8F', '61', '44', '8F', '61', '44', '8F', '61', '44']
wbytes_pat(OutputsHiz_hex, 'OutputsHiz', I2C_ADD)
rbytes_pat(OutputsHiz_hex, 'OutputsHiz_r', I2C_ADD)

LU_code_string = 'E0	0F	0F	34	64	0F	34	64	0F	34	64	0F	34	64	80	80	83	1A	0C	80	02	' \
                 '96	0	0	0	A0	FC	AF	0	0A	24	12	18	0	0	21	E5'
LU_code = re.split('\s+', LU_code_string)
wbytes_pat(LU_code, 'LU_Write', I2C_ADD)
rbytes_pat(LU_code, 'LU_Read', I2C_ADD)

strCFG0 = 'E0 CF 8E 02 14 8E 02 14 8E 02 14 8E 02 14 80 80 84 22 09 0B 85 01 66 00 81 00 A0 FC AF 00 0A 24 18 18 00 00 F5 6D 20 50'
config0 = strCFG0.split()
config0[26] = 'C0'
config0[27] = 'FC'
config0[27] = int(config0[27], 16) & 0b11110111
wbytes_pat(config0, 'writeCFG0', I2C_ADD)
rbytes_pat(config0, 'readCFG0', I2C_ADD, False, 26)

strCFG1 = 'E0 CF 8E 02 14 8E 02 14 8E 02 14 8E 02 14 80 80 04 22 09 00 00 01 66 00 81 00 A0 FC AF 00 0A 24 18 18 00 00 F5 6D 20 50'
config1 = strCFG1.split()
config1[26] = 'C0'
config1[27] = 'FC'
config1[27] = int(config1[27], 16) & 0b11110111
wbytes_pat(config1, 'writeCFG1', I2C_ADD)
rbytes_pat(config1, 'readCFG1', I2C_ADD, False, 26)

htolStr = 'E0 4F BF 11 22 DF 12 14 8E 12 14 8E 12 14 8E 8E 83 1A 0C 80 00 02 96 00 00 00 A0 FC AF 00 FA 38 12 09 00 FF 21 F5'
htol = htolStr.split()
wbytes_pat(htol, "HTOL_Write", I2C_ADD)
rbytes_pat(htol, "HTOL_Read", I2C_ADD)

writeAA_str = 'E0 AA AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA'
writeAA = writeAA_str.split()
wbytes_pat(writeAA, 'write_AA', I2C_ADD)
rbytes_pat(writeAA, 'read_AA', I2C_ADD)

write55_str = 'E0 55 55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55'
write55 = write55_str.split()
wbytes_pat(write55, 'write_55', I2C_ADD)
rbytes_pat(write55, 'read_55', I2C_ADD)

writeAALUT1 = ['AA'] * 65
wbytes_pat(writeAALUT1, 'write_AALUT1', I2C_ADD, 0x30)
rbytes_pat(writeAALUT1, 'read_AALUT1', I2C_ADD, str_byte=0x30)

writeAALUT2 = ['AA'] * 65
wbytes_pat(writeAALUT2, 'write_AALUT2', I2C_ADD, 0x6f)
rbytes_pat(writeAALUT2, 'read_AALUT2', I2C_ADD, str_byte=0x6f)

write55LUT1 = ['55'] * 65
wbytes_pat(write55LUT1, 'write_55LUT1', I2C_ADD, 0x30)
rbytes_pat(write55LUT1, 'read_55LUT1', I2C_ADD, str_byte=0x30)

write55LUT2 = ['55'] * 65
wbytes_pat(write55LUT2, 'write_55LUT2', I2C_ADD, 0x6f)
rbytes_pat(write55LUT2, 'read_55LUT2', I2C_ADD, str_byte=0x6f)

# ============OTP Section==============
currPath = os.getcwd()
os.chdir(currPath + '\OTP\\')
# w1byte_pat(40, 00, 'en_temp_cal', I2C_ADD)
w1byte_pat(40, '28', 'OTP_burn_start', I2C_ADD)
w1byte_pat(40, '20', 'OTP_burn_stop', I2C_ADD)
w1byte_pat(42, '01', 'OTP_start_addr1', I2C_ADD)
w1byte_pat(42, '00', 'OTP_start_addr0', I2C_ADD)
w1byte_pat(44, 37, 'OTP_end_addr37', I2C_ADD)

w1byte_pat(42, 1, 'OTP_start_cfg0', I2C_ADD)
w1byte_pat(44, 0x27, 'OTP_end_cfg0', I2C_ADD)

w1byte_pat(42, 0x28, 'OTP_start_cfg1', I2C_ADD)
w1byte_pat(44, 0x4e, 'OTP_end_cfg1', I2C_ADD)

w1byte_pat(42, 0x4f, 'OTP_start_cfg2', I2C_ADD)
w1byte_pat(44, 0x75, 'OTP_end_cfg2', I2C_ADD)

w1byte_pat(42, 0x76, 'OTP_start_cfg3', I2C_ADD)
w1byte_pat(44, 0x9c, 'OTP_end_cfg3', I2C_ADD)

otpStrEndLut = [0x9d, 0x01, 0x1c, 0x30, 0x30]
wbytes_pat(otpStrEndLut, "OTP_LUT", I2C_ADD, 42)

w1byte_pat(45, '00', 'CSR_bn_addr0', I2C_ADD)
w1byte_pat(45, '01', 'CSR_bn_addr1', I2C_ADD)
w1byte_pat(46, '00', 'CSR_rd_addr0', I2C_ADD)
w1byte_pat(46, '01', 'CSR_rd_addr1', I2C_ADD)
w1byte_pat(45, 26, 'CSR_bn_addr26_band', I2C_ADD)
w1byte_pat(46, 26, 'CSR_rd_addr26_band', I2C_ADD)
w1byte_pat(42, 26, 'OTP_start_addr26_band', I2C_ADD)
w1byte_pat(44, 26, 'OTP_end_addr26_band', I2C_ADD)
# ==================VC3====================
if VC3_FLAG == ('Y' or 'y'):
    os.chdir('..\\..\\..\\code910\\')
    vc3_code = find_vc3_code()
    vc3_divpat = 3
    for i in range(0, vc3_divpat):
        vc3_910 = WritePat("vc3_part%d.atp" % (i + 1))
        vc3_910.write_header('vc3_910_%dto%d' % (i * int(208 / vc3_divpat),
                                                 (i + 1) * int(208 / vc3_divpat)), 'CSCL', 'CSDA')
        vc3_910.write_byte('00', 'Prowrite_CMD')
        if i == (vc3_divpat - 1):
            vc3_910.wbyte_lst(vc3_code, i * (int(208 / vc3_divpat)), 208)
        else:
            vc3_910.wbyte_lst(vc3_code, i * (int(208 / vc3_divpat)), (i + 1) * (int(208 / vc3_divpat)))
        vc3_910.close_pat()
        vc3_910.compile_pat()

        if VC3_LOG_DEL_FLAG == ('Y' or 'y'):
            os.system("del vc3_part%d.atp" % (i + 1))
            os.system("del vc3_part%d.LOG" % (i + 1))

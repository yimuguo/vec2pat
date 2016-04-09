from vec2pat import *
__author__ = 'yguo'
VC3_FLAG = 'N'
VC3_LOG_DEL_FLAG = 'N'
I2C_ADD = 'D0'
os.chdir('S:\Test_Eng\J750_HW_SW\9FGSxxxx\9FGS9091\HTSL\patterns\\' + I2C_ADD)


OutputsHiz_hex = ['E0', '5F', '8F', '61', '44', '8F', '61', '44', '8F', '61', '44', '8F', '61', '44']
wbytes_pat(OutputsHiz_hex, 'OutputsHiz', I2C_ADD)
rbytes_pat(OutputsHiz_hex, 'OutputsHiz_r', I2C_ADD)

LU_code_string = 'E0	0F	0F	34	64	0F	34	64	0F	34	64	0F	34	64	80	80	83	1A	0C	80	02	' \
                 '96	0	0	0	A0	FC	AF	0	0A	24	12	18	0	0	21	E5'
LU_code = re.split('\s+', LU_code_string)
wbytes_pat(LU_code, 'LU_Write', I2C_ADD)
rbytes_pat(LU_code, 'LU_Read', I2C_ADD)

IBM_String = 'E0 4F 8E 12 14 8E 12 14 8E 12 14 8E 12 14 8E 8E 83 1A 0C 80 00 02 96 00 00 00 A0 FC AF 00 0A 24 12 18 00 00 21 E5'
IBM_code = re.split('\s+', IBM_String)
IBM_code[26] = 'C0'
IBM_code[27] = int(IBM_code[27], 16) & 0b11110111
wbytes_pat(IBM_code, 'IBM_Write', I2C_ADD)
rbytes_pat(IBM_code, 'IBM_Read', I2C_ADD, False, 26)

writeAA_str = '80 AA AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA'
writeAA = writeAA_str.split()
wbytes_pat(writeAA, 'write_AA', I2C_ADD)
rbytes_pat(writeAA, 'read_AA', I2C_ADD)

write55_str = '80 55 55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55'
write55 = write55_str.split()
wbytes_pat(write55, 'write_55', I2C_ADD)
rbytes_pat(write55, 'read_55', I2C_ADD)

writeAALUT = ['AA'] * (0xaf-0x30+1)
wbytes_pat(writeAALUT, 'write_AALUT', I2C_ADD, 0x30)
rbytes_pat(writeAALUT, 'read_AALUT', I2C_ADD, str_byte=0x30)

write55LUT = ['55'] * (0xaf-0x30+1)
wbytes_pat(write55LUT, 'write_55LUT', I2C_ADD, 0x30)
rbytes_pat(write55LUT, 'read_55LUT', I2C_ADD, str_byte=0x30)


# ============OTP Section==============
os.chdir('S:\Test_Eng\J750_HW_SW\9FGSxxxx\9FGS9091\HTSL\patterns\\' + I2C_ADD + '\\OTP\\')
# w1byte_pat(40, 00, 'en_temp_cal', I2C_ADD)
w1byte_pat(40, '28', 'OTP_burn_start', I2C_ADD)
w1byte_pat(40, '20', 'OTP_burn_stop', I2C_ADD)
w1byte_pat(42, '01', 'OTP_start_addr1', I2C_ADD)
w1byte_pat(42, '00', 'OTP_start_addr0', I2C_ADD)
w1byte_pat(44, 37, 'OTP_end_addr37', I2C_ADD)

w1byte_pat(42, 1, 'OTP_start_cfg0', I2C_ADD)
w1byte_pat(44, 37, 'OTP_end_cfg0', I2C_ADD)

w1byte_pat(42, 0x26, 'OTP_start_cfg1', I2C_ADD)
w1byte_pat(44, 0x4a, 'OTP_end_cfg1', I2C_ADD)

w1byte_pat(42, 0x4b, 'OTP_start_cfg2', I2C_ADD)
w1byte_pat(44, 0x6f, 'OTP_end_cfg2', I2C_ADD)

w1byte_pat(42, 0x70, 'OTP_start_cfg3', I2C_ADD)
w1byte_pat(44, 0x94, 'OTP_end_cfg3', I2C_ADD)

otpStrEndLut = [0x95, 0x01, 0x14, 0x30, 0x30]
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

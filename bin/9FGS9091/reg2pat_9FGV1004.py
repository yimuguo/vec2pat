from vec2pat import *
__author__ = 'yguo'
VC3_FLAG = 'N'
VC3_LOG_DEL_FLAG = 'N'
I2C_ADD = 'D0'
os.chdir(r"S:\Test_Eng\J750_HW_SW\9FGSxxxx\9FGV1004\HTOL_010\patterns\\")

OutputsHiz = '80 5F 8F 61 44 8F 61 44 8F 61 44 8F 61 44 80 80 83 1A' \
             ' 0C 80 00 02 96 00 00 00 A0 F9 AF 00 0F 24 12 18 00 00 21 F5'
OutputsHiz_hex = re.split('\s+', OutputsHiz)
wbytes_pat(OutputsHiz_hex, 'OutputsHiz', I2C_ADD)
rbytes_pat(OutputsHiz_hex, 'OutputsHiz_r', I2C_ADD)

HTOL_string = '80 4F BF 11 22 DF 12 14 8E 12 14 8E 12 14 8C 8C 83 E0 0A DA A0 01 CA 00 81 00 A0 F9 AF 00 0F 36 08 09 00 00 F6 FD'
HTOL = HTOL_string.split()
wbytes_pat(HTOL, 'HTOL_w', I2C_ADD)
rbytes_pat(HTOL, 'HTOL_r', I2C_ADD)

LU_code_string = '80 0F 0F 01 44 0F 01 44 0F 01 44 0F 01 44 85 85 00 00 ' \
                 '0C 80 00 00 00 00 80 00 A0 39 AF 00 0F 32 19 19 00 00 F1 FD'
LU_code = re.split('\s+', LU_code_string)
wbytes_pat(LU_code, 'LU_code_w', I2C_ADD)
rbytes_pat(LU_code, 'LU_code_r', I2C_ADD)

Default002_string = '00	4F	8F	01	44	8F	01	44	8F	01	44	8F	01	44	85	85	00	00	' \
             '0C	80	00 00	00	00	80	00	A0	39	AF	00	0F	32	19	19	00	00	F5	FD'
Default002 = re.split('\s+', Default002_string)
wbytes_pat(Default002, 'Default002', I2C_ADD)


VOLH_LPHCSL_002_string = '00	4F	8F	01	44	8F	01	44	8F	01	44	8F	01	44	85	85	00	00	' \
             '0C	80	00 00	00	00	81	00	A0	F9	AF	00	0F	32	19	19	00	00	F1	F1 00 10 '
VOLH_LPHCSL_002 = re.split('\s+', Default002_string)
wbytes_pat(VOLH_LPHCSL_002, 'VOLH_LPHCSL_002', I2C_ADD)
# ============OTP Section==============
w1byte_pat(40, 00, 'en_temp_cal', I2C_ADD)
w1byte_pat(40, '08', 'OTP_burn_start', I2C_ADD)
w1byte_pat(40, '00', 'OTP_burn_stop', I2C_ADD)
w1byte_pat(42, '01', 'OTP_start_addr1', I2C_ADD)
w1byte_pat(42, '00', 'OTP_start_addr0', I2C_ADD)
w1byte_pat(44, '37', 'OTP_end_addr37', I2C_ADD)
w1byte_pat(46, '00', 'CSR_bn_addr0', I2C_ADD)
w1byte_pat(46, '01', 'CSR_bn_addr1', I2C_ADD)
w1byte_pat(47, '00', 'CSR_rd_addr0', I2C_ADD)
w1byte_pat(47, '01', 'CSR_rd_addr1', I2C_ADD)

# ==================VC3====================
if VC3_FLAG == ('Y' or 'y'):
    os.chdir('..\\code910\\')
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

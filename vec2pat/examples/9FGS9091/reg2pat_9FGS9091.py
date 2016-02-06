from vec2pat import *
__author__ = 'yguo'
VC3_FLAG = 'N'
VC3_LOG_DEL_FLAG = 'N'
I2C_ADD = 'D0'
os.chdir('S:\Test_Eng\J750_HW_SW\9FGSxxxx\9FGS9091\AKC692-009\\patterns\\')


OutputsHiz_hex = ['80', '5F', '8F', '61', '44', '8F', '61', '44', '8F', '61', '44', '8F', '61', '44']
wbytes_pat(OutputsHiz_hex, 'OutputsHiz', I2C_ADD)
rbytes_pat(OutputsHiz_hex, 'OutputsHiz_r', I2C_ADD)

LU_code_string = '0	0F	0F	34	64	0F	34	64	0F	34	64	0F	34	64	80	80	83	1A	0C	80	0	' \
                 '2	96	0	0	0	A0	FC	AF	0	0A	24	12	18	0	0	21	E5'
LU_code = re.split('\s+', LU_code_string)
wbytes_pat(LU_code, 'LU_Write', I2C_ADD)
rbytes_pat(LU_code, 'LU_Read', I2C_ADD)

IBM_String = '00	4F	83	34	54	83	34	54	83	34	54	83	34	54	80	80	83	1A	0C	80	00	02' \
             '	96	00	00	00	A0	FC	AF	00	0A	24	12	18	00	00	21	E5'
IBM_code = re.split('\s+', IBM_String)
wbytes_pat(IBM_code, 'IBM_Write', I2C_ADD)
rbytes_pat(IBM_code, 'IBM_Read', I2C_ADD)

# ============OTP Section==============
w1byte_pat(40, '28', 'OTP_burn_start', I2C_ADD)
w1byte_pat(40, '20', 'OTP_burn_stop', I2C_ADD)
w1byte_pat(42, '01', 'OTP_start_addr1', I2C_ADD)
w1byte_pat(42, '00', 'OTP_start_addr0', I2C_ADD)
w1byte_pat(44, '37', 'OTP_end_addr37', I2C_ADD)
w1byte_pat(45, '00', 'CSR_bn_addr0', I2C_ADD)
w1byte_pat(45, '01', 'CSR_bn_addr1', I2C_ADD)
w1byte_pat(46, '00', 'CSR_rd_addr0', I2C_ADD)
w1byte_pat(46, '01', 'CSR_rd_addr1', I2C_ADD)

# ==================VC3====================
if VC3_FLAG == ('Y' or 'y'):
    os.chdir('..\\..\\code910\\')
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

from vec2pat import *
__author__ = 'yguo'
I2C_ADD = 'D0'
os.chdir('S:\\Test_Eng\\J750_HW_SW\\9FGSxxxx\\9FGS9091\\patterns\\')


OutputsHiz_hex = ['00', '5F', '8F', '78', '44', '8F', '78', '44', '8F', '78', '44', '8F', '78', '44']
wbytes_pat(OutputsHiz_hex, 'OutputHiz', I2C_ADD)

Default001_string = '00	4F	 87	 38	 44	 87	 38	 44	 87	 38	 44	 87	 38	 44	 85	 85	 83	 1A	 ' \
                    '0C	 80	 00	 02	 96	 00	 00	 00	 A0	 FC	 AF	 00	 0F	 24	 12	 18	 00	 00	 21	 F5'
Default001 = re.split('\s+', Default001_string)
wbytes_pat(Default001, 'Default001', I2C_ADD)
rbytes_pat(Default001, 'Defaultr001', I2C_ADD)

Default002_string = '00	4F	8F	01	44	8F	01	44	8F	01	44	8F	01	44	85	85	00	00	' \
             '0C	80	00 00	00	00	81	00	A0	F9	AF	00	0F	32	19	19	00	00	F5	FD'
Default002 = re.split('\s+', Default002_string)
wbytes_pat(Default002, 'Default002', I2C_ADD)

# ============OTP Section==============
w1byte_pat(40, '28', 'OTP_burn_start', I2C_ADD)
w1byte_pat(40, '20', 'OTP_burn_stop', I2C_ADD)
w1byte_pat(42, '01', 'OTP_start_addr1', I2C_ADD)
w1byte_pat(42, '00', 'OTP_start_addr0', I2C_ADD)
w1byte_pat(44, '37', 'OTP_end_addr37', I2C_ADD)
w1byte_pat(46, '00', 'CSR_bn_addr0', I2C_ADD)
w1byte_pat(46, '01', 'CSR_bn_addr1', I2C_ADD)
w1byte_pat(47, '00', 'CSR_rd_addr0', I2C_ADD)
w1byte_pat(47, '01', 'CSR_rd_addr1', I2C_ADD)

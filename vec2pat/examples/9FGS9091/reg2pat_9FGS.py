from vec2pat import *
__author__ = 'yguo'
I2C_ADD = 'D0'


OutputsHiz_hex = ['00', '5F', '87', '78', '44', '87', '78', '44', '87', '78', '44', '87', '78', '44']
os.chdir('.\\patterns\\')
wbytes_pat(OutputsHiz_hex, 'OutputHiz', I2C_ADD)

Default002_string = '00	4F	8F	01	44	8F	01	44	8F	01	44	8F	01	44	85	85	00	00	' \
             '0C	80	00 00	00	00	81	00	A0	F9	AF	00	0F	32	19	19	00	00	F5	FD'
Default002 = re.split('\s+', Default002_string)
wbytes_pat(Default002, 'Default', I2C_ADD)

# ============OTP Section==============
w1byte_pat(40, '28', 'OTP_burn_start', I2C_ADD)
w1byte_pat(40, '20', 'OTP_burn_stop', I2C_ADD)
w1byte_pat(42, '00', 'OTP_start_addr0', I2C_ADD)
w1byte_pat(44, '37', 'OTP_end_addr37', I2C_ADD)
w1byte_pat(46, '00', 'CSR_bn_addr0', I2C_ADD)
w1byte_pat(46, '01', 'CSR_bn_addr1', I2C_ADD)
w1byte_pat(47, '00', 'CSR_rd_addr0', I2C_ADD)
w1byte_pat(47, '01', 'CSR_rd_addr1', I2C_ADD)

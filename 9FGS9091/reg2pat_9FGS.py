from Lib.reg2pat import *
__author__ = 'yguo'
I2C_ADD = 'D0'


OutputsHiz_hex = ['00', '5F', '87', '78', '44', '87', '78', '44', '87', '78', '44', '87', '78', '44']
os.chdir('.\\patterns\\')
wbytes_pat(OutputsHiz_hex, 'OutputHiz', I2C_ADD)

w1byte_pat(40, '28', 'OTP_burn_start', I2C_ADD)
w1byte_pat(40, '20', 'OTP_burn_stop', I2C_ADD)
w1byte_pat(42, '00', 'OTP_start_addr0', I2C_ADD)
w1byte_pat(44, '37', 'OTP_end_addr37', I2C_ADD)

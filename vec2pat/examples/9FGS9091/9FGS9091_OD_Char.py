from vec2pat import reg2pat
import os
os.chdir('S:\\Test_Eng\\J750_HW_SW\\9FGSxxxx\\9FGS9091\\patterns\\OD_CHAR\\')

for od_ratio in range(8, 25):
    reg2pat.w1byte_pat(33, od_ratio, 'OD_%d' % od_ratio, 'D0')

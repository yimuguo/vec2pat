from vec2pat import *

DEBUG_MODE = 1

VC3_FLAG = 'Y'
VC5_LOG_DEL_FLAG = 'N'
VC3_LOG_DEL_FLAG = 'N'

sample_prg_path = 'S:\\Test_Eng\\J750_HW_SW\\VC5\\AK652_008_760_Cisco\\'

if DEBUG_MODE != 1:
    sample_prg_path = input("   Pleas enter the program path: "
                            "   e.g. \\\corpgroup\\\FTGInfo\\\Test_Eng\\\J750_SW_HW\\\AK652_008_std ")
    VC5_LOG_DEL_FLAG = input("Delete VC5 Pattern Logs and ATP files? Y/N    ")
    VC3_FLAG = input("Does the VC3 needs to be compiled? Y/N    ")
    VC3_LOG_DEL_FLAG = input("Delete VC3 Pattern Logs and ATP files? Y/N    ")

os.chdir(sample_prg_path)

# Read VersaClock 5 Timing Commander Summary
vc5 = VC5Get(os.path.join(sample_prg_path, 'code'))

# Write Writing Register Patterns for all OTP configs
os.chdir('..\\patterns%s\\patsmb\\' % vc5.i2c_address)
for x in range(0, 4):
    if vc5.conf_enable[x] == 1:
        otp_wconfig = WritePat('OTP_wconfig%d.atp' % x, vc5.i2c_address)
        otp_wconfig.write_header('OTP_config%d' % x, 'SCLsel0', 'SDAsel1')
        otp_wconfig.wbyte_lst(vc5.conf[x], 0, int('0x69', 0) + 1)
        otp_wconfig.close_pat()
        otp_wconfig.compile_pat('..\\..\\')
        # Write Reading Register Patterns
        otp_rconfig = WritePat('OTP_rconfig%d.atp' % x, vc5.i2c_address)
        otp_rconfig.write_header('OTP_config%d' % x, 'SCLsel0', 'SDAsel1')
        otp_rconfig.rbyte_lst(vc5.conf[x], 0, int('0x69', 0) + 1)
        otp_rconfig.close_pat()
        otp_rconfig.compile_pat('..\\..\\')

    if VC5_LOG_DEL_FLAG == ('Y' or 'y'):
        os.system("del OTP_wconfig%d.atp" % x)
        os.system("del OTP_wconfig%d.log" % x)
        os.system("del OTP_rconfig%d.atp" % x)
        os.system("del OTP_rconfig%d.log" % x)

# =========================================================================
# VC3_910 External CLk Pattern
# =========================================================================
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

if DEBUG_MODE != 1:
    input("Press ENTER to Exit")

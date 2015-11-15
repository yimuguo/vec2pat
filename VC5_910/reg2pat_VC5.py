from Lib.reg2pat import *
from Lib.vc5_summary import *
sample_prg_path = input("   Pleas enter the program path: "
                        "   e.g. \\\corpgroup\\\FTGInfo\\\Test_Eng\\\J750_SW_HW\\\AK652_008_std ")
# sample_prg_path = '.'
os.chdir(sample_prg_path)

# Read VersaClock 5 Timing Commander Summary
vc5 = VC5Get(os.path.join(sample_prg_path, 'code'))

# Write Writing Register Patterns for all OTP configs
os.chdir('..\\')
for x in range(0, 4):
    if vc5.conf_enable[x] == 1:
        otp_wconfig = WritePat('.\\patterns%s\\patsmb\\OTP_wconfig%d.atp' % (vc5.i2c_address, x), vc5.i2c_address)
        otp_wconfig.write_header('OTP_config%d' % x, 'SCLsel0', 'SDAsel1')
        otp_wconfig.wbyte_lst(vc5.conf[x], 0, int('0x69', 0) + 1)
        otp_wconfig.close_pat()
# Write Reading Register Patterns
        otp_rconfig = WritePat('.\\patterns%s\\patsmb\\OTP_rconfig%d.atp' % (vc5.i2c_address, x), vc5.i2c_address)
        otp_rconfig.write_header('OTP_config%d' % x, 'SCLsel0', 'SDAsel1')
        otp_rconfig.rbyte_lst(vc5.conf[x], 0, int('0x69', 0) + 1)
        otp_rconfig.close_pat()

try:
    for prg_file in glob.glob("*FT*.xls"):
        workbook = prg_file
        print("Compiling against " + workbook + '.....')
        compile_command = "apc .\\patterns%s\\patsmb\\OTP_*.atp " % vc5.i2c_address + \
                          "-digital_inst hsd100200 " \
                          "-suppress_log " \
                          "-extended " \
                          "-comments " \
                          "-pinmap_workbook " + workbook
        os.system(compile_command)
except (NameError, FileNotFoundError):
    sys.exit("No Program WorkBook at directory")

os.chdir('.\\patterns%s\\patsmb\\' % vc5.i2c_address)
del_flag = input("Delete Logs and ATP files? Y/N\n")
if del_flag == 'Y' or 'y':
    os.system("del *.atp")
    os.system("del *.log")
input("press enter to exit")

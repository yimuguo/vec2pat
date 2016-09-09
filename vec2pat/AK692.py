from vec2pat.reg2pat import *
from vec2pat.vc5_crawler import VC5Summary


class AKC692(object):
    cfg_str = []
    cfg_enable = [1, 0, 0, 0]

    def __init__(self, path, i2c_add='D6', vc3=True, del_atp=True):
        self.path = path
        self.i2c_add = i2c_add
        self.del_atp_flg = del_atp
        self.pattern_path = self.path + '/patterns/' + self.i2c_add + '/'
        self.vc3 = vc3

    def generate_pat(self, cfgnum, cfg_string, compile_flg=True):
        config = cfg_string.split()
        config[26] = 'C0'  # VCO band and cal byte
        # config[27] = 'FC' # Force cal byte
        config[27] = int(config[27], 16) & 0b11110111
        # Generate write and compile
        wbytes = WritePat(self.path + '/patterns/' + self.i2c_add + '/writeCFG' + str(cfgnum) + '.atp', self.i2c_add)
        wbytes.write_header('writeCFG' + str(cfgnum))
        wbytes.wbyte_lst(config)
        wbytes.close_pat()
        if compile_flg:
            wbytes.compile_pat(self.path)
        # Generate read and compile
        rbytes = WritePat(self.path + '/patterns/' + self.i2c_add + '/readCFG' + str(cfgnum) + '.atp', self.i2c_add)
        rbytes.vco_mon = False
        rbytes.vco_band_byte = 26
        rbytes.write_header('readCFG' + str(cfgnum))
        rbytes.rbyte_lst(config)
        rbytes.close_pat()
        if compile_flg:
            rbytes.compile_pat(self.path)

    def search_cfg(self, summary_file):
        config_file = VC5Summary(summary_file)
        config_file.file_parser()
        for x in range(0, 4):
            self.cfg_str.append(" ".join(config_file.reg_conf[x]))

    def gen_vc3(self, path='.', wrkbk_path='..', compile_flg=True):
        gen_vc3(path, wrkbk_path, compile_flg, self.del_atp_flg)

    def auto_gen_pat(self):
        cfg_file = ""
        try:
            for file in glob.glob(self.path + "/code/*summary*.txt"):
                cfg_file = file
                break
        except FileNotFoundError:
            print("Config file not found")
            return
        self.search_cfg(cfg_file)
        for cfg in range(0, 4):
            if self.cfg_enable == 1:
                self.generate_pat(cfg, self.cfg_str[cfg])
        if self.vc3:
            self.gen_vc3(self.path+"/patterns/"+self.i2c_add+"/Code910/", self.path)

    def write1byte(self, bytenum, byte, pat_file, compile_flg=True):
        name = 'w1byte'
        w1byte = WritePat(pat_file, self.i2c_add)
        w1byte.write_header(name)
        w1byte.write_byte(bytenum, 'start')
        w1byte.write_byte(byte, 'write_byte_%s' % bytenum)
        w1byte.close_pat()
        if compile_flg:
            w1byte.compile_pat(self.path)

    def misc_pat(self, compile_flg=True, font="int"):
        """
        generate all patterns.
        :param compile_flg: if compile after generate patterns
        :param font: integer options have different otp mappings than FOD versions
        :return: None
        """

        writeAA_str = 'E0 AA AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA	AA'
        writeAA = writeAA_str.split()
        wbytes_pat(writeAA, self.pattern_path + 'write_AA', self.i2c_add, 1, 1)
        rbytes_pat(writeAA, self.pattern_path + 'read_AA', self.i2c_add, str_byte=1, offset=1)

        write55_str = 'E0 55 55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55	55'
        write55 = write55_str.split()
        wbytes_pat(write55, self.pattern_path + 'write_55', self.i2c_add, 1, 1)
        rbytes_pat(write55, self.pattern_path + 'read_55', self.i2c_add, str_byte=1, offset=1)

        OutputsHiz_hex = ['E0', '5F', '8F', '61', '44', '8F', '61', '44', '8F', '61', '44', '8F', '61', '44']
        wbytes_pat(OutputsHiz_hex, 'OutputsHiz', self.i2c_add, 1, 1)
        rbytes_pat(OutputsHiz_hex, 'OutputsHiz_r', self.i2c_add, str_byte=1, offset=1)
        # ============OTP Section==============
        otp_path = self.pattern_path + "OTP\\"
        # w1byte_pat(40, 00, 'en_temp_cal', I2C_ADD)

        self.write1byte(40, '28', otp_path+'OTP_burn_start', compile_flg)
        self.write1byte(40, '20', otp_path+'OTP_burn_stop', compile_flg)
        self.write1byte(42, '01', otp_path+'OTP_start_addr1', compile_flg)
        self.write1byte(42, '00', otp_path+'OTP_start_addr0', compile_flg)
        self.write1byte(44, 37, otp_path+'OTP_end_addr37', compile_flg)

        if font == "int":
            self.write1byte(42, 1, otp_path+'OTP_start_cfg0', compile_flg)
            self.write1byte(44, 37, otp_path+'OTP_end_cfg0', compile_flg)

            self.write1byte(42, 0x26, otp_path+'OTP_start_cfg1', compile_flg)
            self.write1byte(44, 0x4a, otp_path+'OTP_end_cfg1', compile_flg)

            self.write1byte(42, 0x4b, otp_path+'OTP_start_cfg2', compile_flg)
            self.write1byte(44, 0x6f, otp_path+'OTP_end_cfg2', compile_flg)

            self.write1byte(42, 0x70, otp_path+'OTP_start_cfg3', compile_flg)
            self.write1byte(44, 0x94, otp_path+'OTP_end_cfg3', compile_flg)
        else:
            self.write1byte(42, 1, otp_path+'OTP_start_cfg0', compile_flg)
            self.write1byte(44, 0x27, otp_path+'OTP_end_cfg0', compile_flg)

            self.write1byte(42, 0x28, otp_path+'OTP_start_cfg1', compile_flg)
            self.write1byte(44, 0x4e, otp_path+'OTP_end_cfg1', compile_flg)

            self.write1byte(42, 0x4f, otp_path+'OTP_start_cfg2', compile_flg)
            self.write1byte(44, 0x75, otp_path+'OTP_end_cfg2', compile_flg)

            self.write1byte(42, 0x76, otp_path+'OTP_start_cfg3', compile_flg)
            self.write1byte(44, 0x9c, otp_path+'OTP_end_cfg3', compile_flg)

        # otpStrEndLut = [0x9d, 0x01, 0x1c, 0x30, 0x30]
        # wbytes_pat(otpStrEndLut, "OTP_LUT", self.i2c_add, 42)

        self.write1byte(45, '00', otp_path+'CSR_bn_addr0', compile_flg)
        self.write1byte(45, '01', otp_path+'CSR_bn_addr1', compile_flg)
        self.write1byte(46, '00', otp_path+'CSR_rd_addr0', compile_flg)
        self.write1byte(46, '01', otp_path+'CSR_rd_addr1', compile_flg)
        self.write1byte(45, 26, otp_path+'CSR_bn_addr26_band', compile_flg)
        self.write1byte(46, 26, otp_path+'CSR_rd_addr26_band', compile_flg)
        self.write1byte(42, 26, otp_path+'OTP_start_addr26_band', compile_flg)
        self.write1byte(44, 26, otp_path+'OTP_end_addr26_band', compile_flg)


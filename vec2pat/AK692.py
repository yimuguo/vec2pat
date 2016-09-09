from vec2pat.reg2pat import *


class AKC692(object):

    def __init__(self, i2c_add='D6', vc3=True, del_atp=True):
        self.i2c_add = i2c_add

    def generate_pat(self, cfgnum, cfg_string):
        config = cfg_string.split()
        config[26] = 'C0'
        config[27] = 'FC'
        config[27] = int(config[27], 16) & 0b11110111
        wbytes_pat(config, 'writeCFG0', self.i2c_add)
        rbytes_pat(config, 'readCFG0', self.i2c_add, False, 26)


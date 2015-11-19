import re
import os
import sys
import glob


def find_vc3_code(search_path='..\\code910\\'):
    try:
        for file in os.listdir(search_path):
            if file.endswith(".txt"):
                config_file = open(file, mode='rb')
                vec_data = config_file.read()
                vec_string = vec_data.decode('utf-16')
                vec_data = vec_string.split('\r\n')
                for line in vec_data:               # Read Code into List
                    if line[:12] == "<Binary Hex=" and len(line) > 400:
                        hexlist = [line[13:-3][i:i + 2] for i in range(0, len(line[13:-3]), 2)]
                        return hexlist
    except (FileNotFoundError, FileExistsError):
        sys.exit('No Configuration File in Code Folder ' + os.getcwd())


class WritePat(object):
    vco_band_byte = 17
    vco_mon = False

    def __init__(self, pat_file, i2c_address='D4'):
        self.pat_path = os.getcwd()
        self.pat_file = pat_file
        self.pat = open(pat_file, 'w+')
        self.i2c_address = i2c_address
        self.hexinput = i2c_address

    def write_pat(self, tset, scl, sda, label='\t', comment=''):
        if comment == '':
            if label == '\t':
                self.pat.write(str(label) + '\t\t> ' + str(tset) + '\t\t' + str(scl) + '\t' + str(sda) + ';\n')
            elif tset == scl == sda == '':
                self.pat.write(str(label) + '\n')
            else:
                self.pat.write(str(label) + '\t> ' + str(tset) + '\t\t' + str(scl) + '\t' + str(sda) + ';\n')
        else:
            self.pat.write('%s:\t\t\t\t\t//%s\n' % (label, comment))

    def write_header(self, start_label, i2c_clk_tset='SCL', i2c_data_tset='SDA'):
        self.pat.write('import tset bstar, bstop, mack, nack, noop, readt, sack, wridt;\n')
        self.pat.write('\n')
        self.pat.write('vector       ( $tset, %s, %s)\n{\n' % (i2c_clk_tset, i2c_data_tset))    # write i2c
        self.write_pat('', '', '', 'start_label Write_%s:' % start_label)
        self.write_pat('noop', 1, 1)
        self.write_pat('noop', 1, 1, 'repeat 10 ')
        self.write_pat('bstar', 1, 1)
        self.write_byte(self.i2c_address, 'Slave_address')

    def hex2bin_lst(self):
        if type(self.hexinput) is str:
            y = bin(int(self.hexinput, 16))[2:].zfill(8)
            binlist = re.findall('.', y)
        elif type(self.hexinput) is int:
            y = "{0:b}".format(self.hexinput).zfill(8)
            binlist = re.findall('.', y)
        else:
            sys.exit('Input type wrong, either string or number')
        return binlist

    def write_byte(self, hexinput, name=''):
        # if type(hexinput) is list:
        #     for x in hexinput:
        #         y = bin(int(x,16))[2:].zfill(8)
        #         z = re.findall('.', y)
        #         binlist.append(z)
        self.hexinput = hexinput
        binlist = self.hex2bin_lst()
        self.write_pat('', '', '', name, self.hexinput)
        # self.pat.write('%s:\t\t\t\t\t//%s\n' % (name, self.hexinput))
        for i in binlist:
            self.write_pat('wridt', 1, '%s' % i)
        self.write_pat('sack', 1, 'L')

    def read_byte(self, hexinput, name='', last_byte=False):
        # binlist = []
        # if type(hexinput) is list:
        #     for x in hexinput:
        #         y=bin(int(x,16))[2:].zfill(8)
        #         z=re.findall('.',y)
        #         binlist.append(z)
        self.hexinput = hexinput
        binlist = self.hex2bin_lst()
        for n, i in enumerate(binlist):
            if i == ('1' or 1):
                binlist[n] = 'H'
            elif i == ('0' or 0):
                binlist[n] = 'L'
            else:
                sys.exit("Hex String Convert Error")
        self.pat.write('%s:\t\t\t\t\t//%s\n' % (name, self.hexinput))
        self.pat.writelines('\t\t\t> readt\t\t1\t%s;\n' % item for item in binlist)
        if last_byte is True:
            self.write_pat('nack', 1, 1)
        elif last_byte is False:
            self.write_pat('mack', 1, 0)
        else:
            sys.exit()

    def wbyte_lst(self, hexlist, startbyte=0, stopbyte='all'):
        if stopbyte == 'all':
            stopbyte = len(hexlist)
        self.write_byte(int(startbyte), 'Start_w_byte')
        for i in range(int(startbyte), int(stopbyte)):
            self.write_byte(hexlist[i], 'write_byte%s' % hex(i))

    def rbyte_lst(self, hexlist, startbyte=0, stopbyte='all'):
        if stopbyte == 'all':
            stopbyte = len(hexlist)
        self.write_byte(int(startbyte), 'Start_r_byte')
        self.write_pat('noop', 1, 1)
        self.write_pat('bstar', 1, 1)
        self.write_byte(int(self.i2c_address, 16) + 1, 'Restart')
        for i in range(int(startbyte), int(stopbyte) - 1):
            if (self.vco_mon is False) and (i == self.vco_band_byte):
                self.write_pat('', '', '', 'read_byte0x11', 'VCO_band_byte')
                for x in range(0, 8):
                    self.write_pat('readt', 1, 'X')
                self.write_pat('mack', 1, 0)
                continue
            self.read_byte(hexlist[i], 'read_byte%s' % hex(i))
        self.read_byte(hexlist[stopbyte-1], 'read_byte%s' % hex(stopbyte-1), last_byte=True)

    def close_pat(self):
        self.pat.write('\t\t\t> bstop\t\t1\t0;\n')
        self.pat.write('repeat 5\t> noop\t\t1\t1;\nhalt\t\t>\t-\t\t-\t-;\n\t\t\t>\t-\t\t-\t-;\n}')
        self.pat.close()

    def compile_pat(self, workbook_path='..\\'):
        try:
            for workbook in glob.glob(os.path.join(workbook_path, "*FT*.xls")):
                print("Compiling " + os.path.join(self.pat_path, self.pat_file) + "\n"
                      "     against workbook" + workbook + '.....')
                compile_command = "apc %s\\*.atp " % self.pat_path + \
                                  "-digital_inst hsd100200 " \
                                  "-suppress_log " \
                                  "-extended " \
                                  "-comments " \
                                  "-pinmap_workbook " + workbook
                os.system(compile_command)
                break
        except (NameError, FileNotFoundError):
            sys.exit("No Program WorkBook at directory")

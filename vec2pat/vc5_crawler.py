import os
import re
import glob


class VC5Summary(object):

    def __init__(self, summaryfile):
        self.conf = []  # [Config_num, CLK, Freq, Type, VDD, ModRate, Spread(minus Down, positive center)]
        self.conf_enable = [0, 0, 0, 0]
        self.i2c_address = 'D4'
        self.reg_conf = []
        try:
            self.file = open(summaryfile, 'r').readlines()
            print("File opened successfully at " + str(summaryfile))
        except FileExistsError:
            print("File not found " + str(summaryfile))
        self.vco_mon = False

    @staticmethod
    def ln_clk():
        # CLK0 number|---- char33 float floatx number|---- number|-----
        # Refer to TimingCommander Summary File
        clk_ln = re.compile(r'^(CLK[0-4])\s+(\d*\.\d+|\d+|-+)\s+([a-zA-Z]+\d*)\s+(\d\.\d)\s+'
                            r'\d*\.\dx\s+\d\s+(\d*\.\d+|\d+|-+)\s+(0\.\d+|-+)\s+(Down|Center|-+)')
        return clk_ln

    @staticmethod
    def ln_configuration():
        # Match string Configuration 0 to identify a config starts
        ln_conf = re.compile(r'^Configuration ([0-3])$')
        return ln_conf

    @staticmethod
    def ln_break():
        ln = re.compile(r'^-+$')
        return ln

    @staticmethod
    def ln_i2c_add():
        ln = re.compile(r'^Device\s+I2C\s+address:\s+(D[0-9])$')
        return ln

    @staticmethod
    def ln_conf_str():
        ln = re.compile(r'^Configuration\s+[0-4]:\s*[0-9a-fA-F][0-9a-fA-F]\s[0-9a-fA-F][0-9a-fA-F]\s')
        return ln

    def file_parser(self):
        search_clk = self.ln_clk()
        search_conf_ln = self.ln_configuration()
        search_break = self.ln_break()
        search_i2c = self.ln_i2c_add()
        search_reg = self.ln_conf_str()
        conf_num = -1
        i2c_match_flg = False

        for line in range(0, len(self.file)):
            if search_i2c.match(self.file[line]):
                self.i2c_address = search_i2c.search(self.file[line]).group(1)
                i2c_match_flg = True
            elif search_conf_ln.match(self.file[line]):
                if search_break.match(self.file[line+1]):
                    conf_num = search_conf_ln.search(self.file[line]).group(1)
            elif search_clk.match(self.file[line]):
                if conf_num != -1:
                    conf_buffer = self.file[line].split()
                    del conf_buffer[4]
                    del conf_buffer[4]
                    if conf_buffer[6] == 'Down':
                        conf_buffer[5] = '-' + conf_buffer[5]
                    del conf_buffer[6]
                    self.conf.append([conf_num] + conf_buffer + [self.i2c_address])
            elif search_reg.match(self.file[line]):
                reg_buffer = self.file[line].split(':')
                reg_buffer = reg_buffer[1].split()
                self.reg_conf.append(reg_buffer)
                if not i2c_match_flg:
                    if reg_buffer[0] == '61' or reg_buffer[0] == 'E1':
                        self.i2c_address = 'D4'
                    elif reg_buffer[0] == '60' or reg_buffer[0] == 'E0':
                        self.i2c_address = 'D0'
        print("File parsed successfully")


def crawl_directory(parent_dir, file_pattern, depth=1):
    """
    :param parent_dir: Directory Path eg. C:/
    :param file_pattern: *summary*.txt includes wildcard
    :param depth: directory depth
    :return: list of files with full path
    """
    search_dir = parent_dir
    for x in range(0, depth):
        search_dir += "/*"
    search_dir = search_dir + '/' + file_pattern
    return glob.glob(search_dir)


# def fetch_data(path, depth=1):
#     filelst = crawl_directory(path, '*summary*.txt', depth)
#     re_dash_customer = re.compile(r'-*(\d+)\s*\(([A-Za-z-_0-9\s&]+)\)')
#     df = pandas.DataFrame()
#     for file in filelst:
#         device = re.split(r'[/\\]', file)[2]
#         dashcode = re.split(r'[/\\]', file)[-2]
#         customer = 'Unknown'
#         if re_dash_customer.match(dashcode):
#             customer = re_dash_customer.search(dashcode).group(2)
#             dashcode = re_dash_customer.search(dashcode).group(1)
#         elif re.match(r'-+([0-9]+)', dashcode):
#             dashcode = re.search('-+([0-9]+)', dashcode).group(1)
#         vc5 = VC5Summary(file)
#         vc5.file_parser()
#         dfs = pandas.DataFrame(vc5.conf, columns=['Config', 'CLK', 'Freq', 'Type', 'VDD', 'ModRate', 'Spread', 'I2C'])
#         dfs['Dashcode'] = dashcode
#         dfs['Device'] = device
#         dfs['Customer'] = customer
#         df = df.append(dfs)
#     return df

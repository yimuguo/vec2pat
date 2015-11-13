import re
import os
import sys
import glob


def find_vc5_summary(search_path):                  # Read Summary File
    os.chdir(search_path)
    try:
        for file in glob.glob("*summary*.txt"):
            filename = file
            summary_file = open(filename, 'r')
            return summary_file
    except (RuntimeError, TypeError, NameError):
        sys.exit('No Summary Txt File Present')


class InputString(object):

    def __init__(self, hexinput, pat):
        self.hexinput = hexinput
        self.pat = pat

    def write_byte(self, pat, name=''):

        # if type(hexinput) is list:
        #     for x in hexinput:
        #         y = bin(int(x,16))[2:].zfill(8)
        #         z = re.findall('.', y)
        #         binlist.append(z)

        if type(self.hexinput) is str:
            y = bin(int(self.hexinput, 16))[2:].zfill(8)
            binlist = re.findall('.', y)
        elif type(self.hexinput) is int:
            y = "{0:b}".format(self.hexinput).zfill(8)
            binlist = re.findall('.', y)
        else:
            sys.exit('Input type wrong, either string or number')
        self.pat.write('%s:\t\t\t\t\t//%s\n' % (name, self.hexinput))
        self.pat.writelines('\t\t\t> wridt\t\t1\t%s;\n' % item for item in binlist)
        self.pat.write('\t\t\t> sack\t\t1\tL;\n')

    def read_byte(self, pat, name=''):
        binlist = []
        '''
        if type(hexinput) is list:
            for x in hexinput:
                y=bin(int(x,16))[2:].zfill(8)
                z=re.findall('.',y)
                binlist.append(z)
        '''
        if type(self.hexinput) is str:
            y = bin(int(self.hexinput, 16))[2:].zfill(8)
            binlist = list(y)
            for n, i in enumerate(binlist):
                if i == '1':
                    binlist[n] = 'H'
                elif i == '0':
                    binlist[n] = 'L'
                else:
                    sys.exit("Hex String Convert Error")
        elif type(self.hexinput) is int:
            y = "{0:b}".format(self.hexinput).zfill(8)
            binlist = list(y)
            for n, i in enumerate(binlist):
                if i == 1:
                    binlist[n] = 'H'
                elif i == 0:
                    binlist[n] = 'L'
                else:
                    sys.exit("Hex String Convert Error")
        else:
            print('Input type wrong, either string or number')
        self.pat.write('%s:\t\t\t\t\t//%s\n' % (name, self.hexinput))
        self.pat.writelines('\t\t\t> readt\t\t1\t%s;\n' % item for item in binlist)
        self.pat.write('\t\t\t> mack\t\t1\t0;\n')

import os
import sys
import glob
import re


class VC5Get(object):
    conf = []
    output_freq = []
    conf_enable = [0, 0, 0, 0]
    # conf_string = []
    vdd = []
    i2c_address = 'D4'

    def __init__(self, search_path='.//', process=1, vco_mon=False):                  # Read Summary File
        os.chdir(search_path)
        try:
            for file in glob.glob("*summary*.txt"):
                filename = file
                self.summary_file = open(filename, 'r')
                self.vco_mon = vco_mon
                if process == 1:
                    self.process_file()
                break
        except():
            sys.exit('No Summary Txt File Present')

    def process_file(self):
        search_for = ['CLK0', 'CLK1', 'CLK2', 'CLK3', 'CLK4']
        for line in self.summary_file:
            if any(x in line for x in search_for):      # Read Frequency Across Configs
                line = re.split('\s+', line)
                self.output_freq.append(line[1])
                self.vdd.append(line[3])
            elif ("Configuration" in line) and (len(line) > 20):
                line = re.split('\s+', line)            # Read Config Hex Strings and Correct I2C Address for TC
                if line[2] == 'E0':
                    line[2] = '60'
                elif line[2] == 'E1':
                    line[2] = '61'
                if line[2] == '60':
                    self.i2c_address = 'D0'
                line = line[2:]
                if self.vco_mon is False:
                    line[0x11] = '3F'
                    line[0x1c] = str(hex(int(line[0x1c], 16) & 0b01111111).zfill(2))[2:]
                    line[0x1d] = str(hex(int(line[0x1d], 16) & 0b11111101).zfill(2))[2:]
                    line[0x16] = str(hex(int(line[0x16], 16) & 0b11110111).zfill(2))[2:]
                # self.conf_string = ' '.join(line)
                self.conf.append(line)

        for i in range(0, 4):
            for x in range(int(len(self.output_freq) / 4)*i, (1+i)*int(len(self.output_freq) / 4)):
                if self.output_freq[x] != '-----':
                    self.conf_enable[i] = 1
                    break

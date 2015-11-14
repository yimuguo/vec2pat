import os
import sys
import glob
import re


class VC5Get(object):
    def __init__(self, search_path='.//'):                  # Read Summary File
        os.chdir(search_path)
        try:
            for file in glob.glob("*summary*.txt"):
                filename = file
                self.summary_file = open(filename, 'r')
        except (RuntimeError, TypeError, NameError):
            sys.exit('No Summary Txt File Present')

    def process_file(self):
        conf_string = []
        conf = []
        output_freq = []
        conf_enable = [0, 0, 0, 0]
        search_for = ['CLK0', 'CLK1', 'CLK2', 'CLK3', 'CLK4']
        for line in self.summary_file:
            if any(x in line for x in search_for):      # Read Frequency Across Configs
                line = re.split('\s+', line)
                output_freq.append(line[1])
            elif ("Configuration" in line) and (len(line) > 20):
                line = re.split('\s+', line)            # Read Config Hex Strings and Correct I2C Address for Timing Commander
                if line[2] == 'E0':
                    line[2] = '60'
                elif line[2] == 'E1':
                    line[2] = '61'
                line = line[2:]
                conf_string = ' '.join(line)
                conf.append(conf_string)
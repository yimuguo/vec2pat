#!/usr/bin/python
import re
import os
import sys
import glob

try:
    for file in os.listdir(".\\patternsD4\\code910\\"):
        if file.endswith(".txt"):
            ConfigFile = open(os.path.join(".\\patternsD4\\code910\\", file), mode='rb')
            vec_data = ConfigFile.read()
            vec_string = vec_data.decode('utf-16')
            vec_data = vec_string.split('\r\n')
            for line in vec_data:               # Read Code into List
                if line[:12] == "<Binary Hex=" and len(line) > 400:
                    hexlist = [line[13:-3][i:i + 2] for i in range(0, len(line[13:-3]), 2)]
                    break
except RuntimeError:
    sys.exit('No Configuration File in Code Folder')

# Write Binary Data to Pattern Format


def write8b(name, hexinput, pat):
    binlist = []
    '''
    if type(hexinput) is list:
        for x in hexinput:
            y=bin(int(x,16))[2:].zfill(8)
            z=re.findall('.',y)
            binlist.append(z)
    '''
    if type(hexinput) is str:
        y = bin(int(hexinput, 16))[2:].zfill(8)
        binlist = re.findall('.', y)
    elif type(hexinput) is int:
        y = "{0:b}".format(hexinput).zfill(8)
        binlist = re.findall('.', y)
    else:
        print('Input type wrong, either string or number')
    pat.write('%s:\t\t\t\t\t//%s\n' % (name, hexinput))
    pat.writelines('\t\t\t> wridt\t\t1\t%s;\n' % item for item in binlist)
    pat.write('\t\t\t> sack\t\t1\tL;\n')


def bytex2y(x, y):
    startbit = int(x)
    address = 'D4'
    pat_file = '.\\patternsD4\\code910\\register%sto%s.atp' % (x, y)
    # os.makedirs(os.path.dirname(pat_file), exist_ok=True)
    pat = open(pat_file, 'w+')
    pat.write('import tset bstar, bstop, mack, nack, noop, readt, sack, wridt;\n')
    pat.write('\n')
    pat.write('vector       ( $tset, CSCL, CSDA)\n{\nstart_label Write_B%s_to_B%s:\n' % (x, y))
    pat.write('\t\t\t> noop\t\t1\t1;\nrepeat 10\t> noop\t\t1\t1;\n\t\t\t> bstar\t\t1\t1;\n')

    write8b('Slave_address', address, pat)
    write8b('Prowrite_CMD', '00', pat)
    write8b('Start_w_byte', startbit, pat)
    # i = x
    for i in range(x, y):
        write8b('write_byte_%d' % i, hexlist[i], pat)
        i += 1
    pat.write('\t\t\t> bstop\t\t1\t0;\n')
    pat.write('repeat 5\t> noop\t\t1\t1;\nhalt\t\t>\t-\t\t-\t-;\n\t\t\t>\t-\t\t-\t-;\n}')
    pat.close()
# bytex2y(0,208)
bytex2y(0, 51)
bytex2y(51, 101)
bytex2y(101, 150)
bytex2y(150, 208)

os.chdir('.')
try:
    for prg_file in glob.glob("*FT*.xls"):
        workbook = prg_file
        print("Compiling against " + workbook)
        compile_command = "apc .\\patternsD4\\code910\\register*.atp " \
                          "-digital_inst hsd100200 " \
                          "-suppress_log " \
                          "-extended " \
                          "-pinmap_workbook " + workbook
        os.system(compile_command)
        os.chdir('.\\patternsD4\\code910\\')
        del_flag = input("Delete Logs and ATP files? Y/N\n")
        if del_flag == 'Y' or 'y':
            os.system("del *.atp")
            os.system("del *.log")
        input("press enter to exit")
except NameError:
    sys.exit("No Program WorkBook at directory")

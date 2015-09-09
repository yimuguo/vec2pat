#!/usr/bin/python
import re
import os
import sys
# vec_file = "..\\VC5_910\\registerhex_910\\vec.txt"


for file in os.listdir(".\\code\\"):
    if file.endswith(".txt"):
        ConfigFile = open(os.path.join(".\\code\\", file), mode = 'rb')
        vec_data = ConfigFile.read()
        vec_string = vec_data.decode('utf-16')
        vec_data = vec_string.split('\r\n')
        break
    else:
        sys.exit('No Configuration File in Code Folder')
        
for line in vec_data:
    if line[:12] == "<Binary Hex=" and len(line) > 400:
        hexlist = re.findall('..', line[13:-3])


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


######## Get all vector separated into list#######


def read8b(name, hexinput, pat):
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
        for n,i in enumerate(binlist):
            if i == '1':
                binlist[n] = 'H'
            elif i == '0':
                binlist[n] = 'L'
            else:
                sys.exit("Hex String Convert Error")
    elif type(hexinput) is int:
        y = "{0:b}".format(hexinput).zfill(8)
        binlist = re.findall('.', y)
        for n, i in enumerate(binlist):
            if i == 1:
                binlist[n] = 'H'
            elif i == 0:
                binlist[n] = 'L'
            else:
                sys.exit("Hex String Convert Error")
    else:
        print('Input type wrong, either string or number')
    pat.write('%s:\t\t\t\t\t//%s\n' % (name, hexinput))
    pat.writelines('\t\t\t> readt\t\t1\t%s;\n' % item for item in binlist)
    pat.write('\t\t\t> mack\t\t1\t0;\n')


def writeregx2y(x, y):
    startbit = int(x)
    address = 'D4'
    pat_file = '.\\patterns\\patsmb\\write%sto%s.atp' % (x, y)
    os.makedirs(os.path.dirname(pat_file), exist_ok=True)
    pat = open(pat_file, 'w+')
    pat.write('import tset bstar, bstop, mack, nack, noop, readt, sack, wridt;\n')
    pat.write('\n')
    pat.write('vector       ( $tset, SCL, SDA)\n{\nstart_label Write_B%s_to_B%s:\n' % (x,y))
    pat.write('\t\t\t> noop\t\t1\t1;\nrepeat 10\t> noop\t\t1\t1;\n\t\t\t> bstar\t\t1\t1;\n')

    write8b('Slave_address', address, pat)
    write8b('Prowrite_CMD', '00', pat)
    write8b('Start_w_byte', startbit, pat)
    for i in range(x, y):
        write8b('write_byte_%d' % i, hexlist[i], pat)
    pat.write('\t\t\t> bstop\t\t1\t0;\n')
    pat.write('repeat 5\t> noop\t\t1\t1;\nhalt\t\t>\t-\t\t-\t-;\n\t\t\t>\t-\t\t-\t-;\n}')
    pat.close()


writeregx2y(0, 51)
writeregx2y(51, 101)
writeregx2y(101, 150)
writeregx2y(150, 208)


def readregx2y(x, y):
    startbit = int(x)
    address = 'D4'
    pat = open('.\\patterns\\patsmb\\read%sto%s.atp' % (x, y), 'w+')

    pat.write('import tset bstar, bstop, mack, nack, noop, readt, sack, wridt;\n')
    pat.write('\n')
    pat.write('vector       ( $tset, SCL, SDA)\n{\nstart_label Write_B%s_to_B%s:\n' % (x, y))
    pat.write('\t\t\t> noop\t\t1\t1;\nrepeat 10\t> noop\t\t1\t1;\n\t\t\t> bstar\t\t1\t1;\n')

    write8b('Slave_address', address, pat)
    write8b('Prowrite_CMD', '00', pat)
    write8b('Start_r_byte', startbit, pat)
    pat.write('\t\t\t> noop\t\t1\t1;\n\t\t\t> bstar\t\t1\t1;\n')
    write8b('Restart', 'D5', pat)
    read8b('ID_Byte', '10', pat)
    for i in range(x, y-1):
        if 82 <= i <= 85:
            read8b('read_byte_%d' % i, hexlist[81], pat)
        elif 124 <= i <= 127:
            read8b('read_byte_%d' % i, hexlist[123], pat)
        else:
            read8b('read_byte_%d' % i, hexlist[i], pat)
    last_hex = bin(int(hexlist[y-1], 16))[2:].zfill(8)
    last_byte = re.findall('.', last_hex)
    for n, i in enumerate(last_byte):
        if i == '1':
            last_byte[n] = 'H'
        elif i == '0':
            last_byte[n] = 'L'
        else:
            sys.exit("Last Byte Wrong")
    pat.write('%s:\t\t\t\t\t//%s\n' % ('read_byte_%d' % (y - 1), hexlist[y-1]))
    pat.writelines('\t\t\t> readt\t\t1\t%s;\n' % item for item in last_byte)
    pat.write('\t\t\t> nack\t\t1\t1;\n')

    pat.write('\t\t\t> bstop\t\t1\t0;\n')
    pat.write('\t\t\t> noop\t\t1\t1;\nhalt\t\t>\t-\t\t-\t-;\n\t\t\t>\t-\t\t-\t-;\n}')
    pat.close()

readregx2y(0, 51)
readregx2y(51, 101)
readregx2y(101, 150)
readregx2y(150, 208)

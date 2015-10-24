import os
__author__ = 'yguo'


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
        binlist = list(y)
        for n, i in enumerate(binlist):
            if i == '1':
                binlist[n] = 'H'
            elif i == '0':
                binlist[n] = 'L'
            else:
                os.error("Hex String Convert Error")
    elif type(hexinput) is int:
        y = "{0:b}".format(hexinput).zfill(8)
        binlist = list(y)
        for n, i in enumerate(binlist):
            if i == 1:
                binlist[n] = 'H'
            elif i == 0:
                binlist[n] = 'L'
            else:
                os.error("Hex String Convert Error")
    else:
        print('Input type wrong, either string or number')
    pat.write('%s:\t\t\t\t\t//%s\n' % (name, hexinput))
    pat.writelines('\t\t\t> readt\t\t1\t%s;\n' % item for item in binlist)
    pat.write('\t\t\t> mack\t\t1\t0;\n')


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
        binlist = list(y)
    elif type(hexinput) is int:
        y = "{0:b}".format(hexinput).zfill(8)
        binlist = list(y)
    else:
        print('Input type wrong, either string or number')
    pat.write('%s:\t\t\t\t\t//%s\n' % (name, hexinput))
    pat.writelines('\t\t\t> wridt\t\t1\t%s;\n' % item for item in binlist)
    pat.write('\t\t\t> sack\t\t1\tL;\n')


def writeregx2y(x, y):
    startbit = int(x)
    address = 'D0'
    pat_file = '.\\patterns\\patdc\\write%sto%s.atp' % (x, y)
    os.makedirs(os.path.dirname(pat_file), exist_ok=True)
    pat = open(pat_file, 'w+')
    pat.write('import tset bstar, bstop, mack, nack, noop, readt, sack, wridt;\n')
    pat.write('\n')
    pat.write('vector       ( $tset, SCL, SDA)\n{\nstart_label Write_B%s_to_B%s:\n' % (x, y))
    pat.write('\t\t\t> noop\t\t1\t1;\nrepeat 10\t\t> noop\t\t1\t1;\n\t\t\t> bstar\t\t1\t1;\n')

    write8b('Slave_address', address, pat)
    # write8b('Prowrite_CMD', '00', pat)
    write8b('Start_w_byte', startbit, pat)
    for i in range(x, y):
        write8b('write_byte_%d' % i, hexlist[i], pat)
    pat.write('\t\t\t> bstop\t\t1\t0;\n')
    pat.write('repeat 5\t> noop\t\t1\t1;\nhalt\t\t>\t-\t\t-\t-;\n\t\t\t>\t-\t\t-\t-;\n}')
    pat.close()

hexlist = ['00', '5F', '87', '78', '44', '87', '78', '44', '87', '78', '44', '87', '78', '44']
writeregx2y(1, 14)


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
                sys.exit("Hex String Convert Error")
    elif type(hexinput) is int:
        y = "{0:b}".format(hexinput).zfill(8)
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


__author__ = 'yguo'
import re

pat = open("i2c_write.atp", "w+")
# define timing sets and vector and start write address
TSD = 'tset bstar, bstop, mack, nack, noop, readt, sack, wridt'
vector = '$test, CSCL, CSDA'
i2c_add = 'D0'
start_add = '00'
# write timing sets and vector
pat.write('import %s\n\n' % TSD)
pat.write('vector\t\t(%s)\n{\n' % vector)


def write1byte(name, hexinput, pat):
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

write1byte("Slave_Address", i2c_add, pat)
write1byte("Start_Address", start_add, pat)

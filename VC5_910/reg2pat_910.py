#!/usr/bin/python
import re
vec_file=".\\VC5_910\\registerhex_910\\vec.txt"
with open(vec_file,'r') as vec_data:
    vec=vec_data.read().splitlines()
vec=vec[0]

########Write Binary Data to Pattern Format
def write8b(name,hexinput,pat):
    binlist=[]
    '''
    if type(hexinput) is list:
        for x in hexinput:
            y=bin(int(x,16))[2:].zfill(8)
            z=re.findall('.',y)
            binlist.append(z)
    '''
    if type(hexinput) is str:
        y=bin(int(hexinput,16))[2:].zfill(8)
        binlist=re.findall('.',y)
    elif type(hexinput) is int:
        y="{0:b}".format(hexinput).zfill(8)
        binlist=re.findall('.',y)
    else:
        print 'Input type wrong, either string or number'
    pat.write('%s:\t\t\t\t\t//%s\n' % (name,hexinput))
    pat.writelines('\t\t\t> wridt\t\t1\t%s;\n' % item for item in binlist)
    pat.write('\t\t\t> sack\t\t1\tL;\n')

########Get all vector seperated into list#######
hexlist=re.findall('..',vec)
del vec

def bytex2y(x,y):
    startbit=int(x)
    address='D4'
    pat=open('.\\VC5_910\\patterns\\register%sto%s.atp' %(x,y),'w+')
    pat.write('import tset bstar, bstop, mack, nack, noop, readt, sack, wridt;\n')
    pat.write('\n')
    pat.write('vector       ( $tset, CSCL, CSDA)\n{\nstart_label Write_B%s_to_B%s:\n' % (x,y))
    pat.write('\t\t\t> noop\t\t1\t1;\nrepeat 10\t> noop\t\t1\t1;\n\t\t\t> bstar\t\t1\t1;\n')
    
    write8b('Slave_address',address,pat)
    write8b('Prowrite_CMD','00',pat)
    write8b('Start_w_byte',startbit,pat)
    i=x
    for i in xrange(x,y):
        write8b('write_byte_%d' % i,hexlist[i],pat)
        i+=1
    pat.write('\t\t\t> bstop\t\t1\t0;\n')
    pat.write('repeat 5\t> noop\t\t1\t1;\nhalt\t\t>\t-\t\t-\t-;\n\t\t\t>\t-\t\t-\t-;\n}')
    pat.close()
#bytex2y(0,208)
#bytex2y(0,51)
bytex2y(51,101)
#bytex2y(101,150)
#bytex2y(150,200)
#bytex2y(200,208)
#print l
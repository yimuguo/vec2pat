#!/usr/bin/python
import re
vec_file='vec.txt'
with open(vec_file,'r') as vec_data:
    vec=vec_data.read().splitlines()
vec=vec[0]


########Get all vector seperated into list#######
hexlist=re.findall('..',vec)
del vec
binlist=[]


########Convert Hex to Bin
for x in hexlist:
    #y=hex_to_binary(x)
    y=bin(int(x,16))[2:].zfill(8)
    #y="{0:8b}".format(int(x,16))
    binlist.append(y)


########Split Binary List into final output list to print
l=[]
for x in binlist:
    y=re.findall('.',x)
    l.append(y)


########Write Binary Data to Pattern Format
def write8b(name,list,file):
    pat=open(file,'a+')
    pat.write('%s:\t\t\t\t//%s\n' % (name)
    pat.write('\t\t\t> wridt\t1\t%s;\n' % list[0])
    i=0
    for i in range(1,len(list)):
        pat.write('\t\t\t>\t-\t\t1\t%s;\n' % list[i])
        i+=1

def bytex2y(x,y):
    address='D4'
    add_bin=bin(int(address,16))[2:].zfill(8)
    add_bin_split=re.findall('.',add_bin)
    pat=open('pat%sto%s.txt' %(x,y),'w+')
    pat.write('import tset bstar, bstop, mack, nack, noop, readt, sack, wridt;\n')
    pat.write('\n')
    pat.write('vector       ( $tset, CSCL, CSDA)\n{\nstart_label Write_B%s_to_B%s:\n' % (x,y))
    pat.write('\t\t\t> noop\t\t1\t1;\nrepeat_10\t> noop\t\t1\t1;\n\t\t\t> bstar\t\t1\t1;\nI2C Slave Address:\t\t\t\t\t\t//%s\n' % address)

    pat.writelines('\t\t\t> wridt\t\t1\t%s;\n' % item for item in add_bin_split)
    pat.write('\t\t\t> sack\t\t1\tL;\n')
    
    pat.write('Prowrite_CMD:\t\t\t\t\t\t\t//00\n' )
    prowrite=bin(int('00',16))[2:].zfill(8)
    prowrite_split=re.findall('.',prowrite)
    pat.writelines('\t\t\t> wridt\t\t1\t%s;\n' % item for item in prowrite_split)
    pat.write('\t\t\t> sack\t\t1\tL;\n')
    
    pat.write('Start_write_byte:\t\t\t\t\t\t\t//%s\n' % x)
    startadd="{0:b}".format(int(x)).zfill(8)
    startadd_split=re.findall('.',prowrite)
    pat.writelines('\t\t\t> wridt\t\t1\t%s;\n' % item for item in startadd)
    pat.write('\t\t\t> sack\t\t1\tL;\n')
    
    i=x
    for i in xrange(x,y):
        pat.write('write_byte_%d:\t\t\t\t\t\t\t//%s\n\t\t\t> wridt\t\t1\t%s;\n' % (i,hexlist[i],l[i][0]))
        for m in xrange(1,len(l[i])):
            pat.write('\t\t\t>\t-\t\t1\t%s;\n' % l[i][m])
        pat.write('\t\t\t> sack\t\t1\tL;\n')
        i+=1
    pat.write('repeat_5\t> noop\t\t1\t1;\nhalt\t\t>\t-\t\t-\t-;\n\t\t\t>\t-\t\t-\t-;\n}')
    pat.close()
#bytex2y(0,208)
#bytex2y(0,51)
bytex2y(51,101)
#bytex2y(101,150)
#bytex2y(150,200)
#bytex2y(200,208)
#print l
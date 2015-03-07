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

pat=open('pat.txt','w+')
pat.write('import tset bstar, bstop, mack, nack, noop, readt, sack, wridt;\n')
pat.write('\n')
pat.write('vector       ( $tset, CSCL, CSDA)\n{\nstart_label Write_B0_to_B50:\n')
i=0
for x in l:
    pat.write('write_byte_%d:\t\t\t\t\t//%s\n\t\t\t> wridt\t\t1\t%s\n' % (i,hexlist[i],l[i][0]))
    for m in xrange(1,len(x)):
        pat.write('\t\t\t>\t-\t\t1\t%s\n' % l[i][m])
    pat.write('\t\t\t> sack\t\t1\tL\n')
    i+=1
pat.close()
#print l
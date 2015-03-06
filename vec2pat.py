#!/usr/bin/python
import re
import binascii
vec_file='vec.txt'
with open(vec_file,'r') as vec_data:
    vec=vec_data.read().splitlines()
vec=vec[0]
#bin=binascii.unhexlify(vec)
#bin=re.findall('.',bin)
hex=re.findall('..',vec)
bin=[]
for x in hex:
    a=binascii.a2b_hqx(x)
    y="{0:8b}".format(int(x,16))
    bin.append(y)
print len(vec)
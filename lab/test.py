import base64
import binascii
from operator import xor
def asciitohex(ascii):
    return binascii.b2a_hex(ascii)
def hextoascii(hex):
    return binascii.a2b_hex(hex)

def hextobase(hex):
    return binascii.b2a_base64(hex)
def basetohex(base):
    return binascii.a2b_base64(base)
def strxor(str1,key): #assumes hex encoded
    a=int(str1, 16)
    b=int(key,16)
    if a.len()> b.len():
        

    
    
f = open('test.txt','r')
for line in f:
    print (line)
    print (strxor(line,line))



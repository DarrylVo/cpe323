import base64
import binascii
from operator import xor
def asciitohex(ascii):
    return base64.b16encode(ascii)
def hextoascii(hex):
    return base64.b16decode(hex, casefold=True)
def basetohex(base):
    base = base64.b64decode(base)
    return base64.b16encode(base)
def hextobase(hex):
    hex = base64.b16decode(hex,casefold=True)
    return base64.b64decode(hex)
def strxor(str1, key):
    z= 1;
    for a in str1:
        
    
    
f = open('test.txt','r')

for line in f:
    print (line)
    a=hextoascii(line[:-1])
    strxor(a,a)
    
    #a = line.decode("hex")


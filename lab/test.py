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
def strxor(str1, key, bytes = 1): #ONLY WORKS FOR ONE BYTE ATM, ASSUME ASCII
    z= 0
    ret = ''
    
    for a in str1:
        ret+= chr(ord(a)^ord(key))
        
    return ret

def stranalyze(str1): #ASSUME ASCII
    counter = 0;
  
    e = 0;
   
    for chrs in str1:
        counter+=1
        
        if ord(chrs) == ord('e'):
            e+=1
    
    e= float(e)/counter
   
    
    if((e>0.06)):
        return True

f = open('C.txt','r')

for line in f:
    
    a=base64.b64decode(line[:-1])
    building = bytearray(40)
    for y in range(0,5):
        
        for x in range(0,256):
            building[y] = x
            b = strxor(a,building,bytes = y+1)
           
            if(stranalyze(b)==True):
                print b
''' 
f = open('B.txt','r')
for line in f:
    a=hextoascii(line[:-1])
    for x in range(0,256):
        
        b = strxor(a,chr(x))
       
        if(stranalyze(b)==True):
            print b
def strxorzzz(str1, key, bytes = 1): #ONLY WORKS FOR ONE BYTE ATM, ASSUME ASCII
    z= 0
    ret = ''
    
    for a in str1:
        ret+= chr(ord(a)^ord(key))
        
    return ret
'''

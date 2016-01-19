import base64
import binascii
import sys
import struct




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
def strxor(str1, key, numb): #ONLY WORKS FOR ONE BYTE ATM, ASSUME ASCII
    ret = ''
    counter = 0
    for a in str1:
        ret+= chr(ord(a)^ord(key[counter]))
        counter+=1
        if counter > numb:
            counter = 0
        
    return ret

def stranalyze(str1): #ASSUME ASCII
    
    counter = 0;
    a = 0;
    e = 0;
    
   
    for chrs in str1:
        counter+=1
        
        if (ord(chrs) == ord('a'))|(ord(chrs) == ord('A')):
            a+=1
        if (ord(chrs) == ord('e'))|(ord(chrs) == ord('E')):
            e+=1
        
    a= float(a)/counter
    e= float(e)/counter
    
   
    
    if((e>0.05)&(a>0.03)):
        return True

    

f = open('C.txt','r')

line = f.read()

a=base64.b64decode(line[:-1])


for x in range(1500000,4000000):

    b = struct.pack("I",x)
    for l in range(0,4):
        c = strxor(a,b,l)
        if (stranalyze(c)==True):
            print c




    

                

            
'''      

f = open('B.txt','r')

for line in f:
    a=hextoascii(line[:-1])
    for x in range(0,256):

        b = struct.pack("I",x)
        for l in range(0,4):
            c = strxor(a,b,l)
            if (stranalyze(c)==True):
                print c
    
    
    
def strxorzzz(str1, key, bytes = 1): #ONLY WORKS FOR ONE BYTE ATM, ASSUME ASCII
    z= 0
    ret = ''
    
    for a in str1:
        ret+= chr(ord(a)^ord(key))

    return ret
'''

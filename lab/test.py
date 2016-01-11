import base64

def asciitohex(ascii):
   return base64.b16encode(ascii)  

def hextoascii(hex):
   return base64.b16decode(hex)

def base64tohex(base):
   a= base64.b64decode(base)
   return base64.b16encode(a)
   

def hextobase64(hex):
   a = base64.b16decode(hex)
   return base64.standard_b64encode(a)
#chr() ord()
print 'start: Man'
a = asciitohex('Man')
print 'ascii to hex: '+a 
b = hextoascii(a)
print 'hex to ascii: '+b
c = hextobase64(a)
print 'hextobase64:'+c +":" 
print 'base64tohex:'+base64tohex(c)

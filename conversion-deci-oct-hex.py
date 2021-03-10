
dec =int(input("enter the number"))
def convert(dec):
    binary=bin(dec)
    octal=oct(dec)
    hexadecimal=hex(dec)
    return(binary,octal,hexadecimal)
bin,oct,hex=convert(dec)
print("binary={},octal={},hexadecimal={}".format(bin,oct,hex))


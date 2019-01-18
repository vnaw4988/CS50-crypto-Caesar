import sys
import cs50
 
# User Input here
if (len(sys.argv) != 3 ):
     sys.exit("Usage: caesar <key> hello")
 
key = int(sys.argv[1])
mystr = str(sys.argv[2])
newstr = []
 
#bytearray(mystring)
 
print(mystr)
print(key)
 
length = len(mystr)
 
for i in range(length):
    #print(ord(mystring[i]))
    #print(chr(104), chr(101))
    if ord(mystr[i]) > 64 and ord(mystr[i]) < 91:
        newstr.append(chr( ((ord(mystr[i]) - 65 + key)%26)+65 ))
        print(chr( ((ord(mystr[i]) - 65 + key)%26)+65 ))
    elif ord(mystr[i]) > 96 and ord(mystr[i]) < 123:
        newstr.append(chr( ((ord(mystr[i]) - 97 + key)%26)+97 ))
 
print("".join(newstr))

from binascii import hexlify

os = file("Image.img", 'rb')

# creates my hex file that I can examine in a hex editor. 
image = open("Image.img","rb")
hexs = hexlify(image.read())
h = open("binary.txt","wb")
h.write(str(hexs))
h.close()

# Starts at index 11 and reads two bytes of information
bi = os.read(11)
bi = os.read(2)
sub2 = str("{0:0>2}".format(ord(bi[1]), "x")) + str("{0:0>2}".format(ord(bi[0]), "x"))
a2 = int(sub2,16)

# Reads byte 13
bi = os.read(1)
sub3 = str("{0:0>2}".format(ord(bi[0]), "x"))
a3 = int(sub3,16)

# Reades byte 14 and 15
bi = os.read(2)
sub4 = str("{0:0>2}".format(ord(bi[1]), "x")) + str("{0:0>2}".format(ord(bi[0]), "x"))
a4 = int(sub4,16)

# Reads byte 16
bi = os.read(1)
sub5 = str("{0:0>2}".format(ord(bi[0]), "x"))
a5 = int(sub5,16)

# Reads bytes 17 and 18
bi = os.read(2)
sub6 = str("{0:0>2}".format(ord(bi[1]), "x")) + str("{0:0>2}".format(ord(bi[0]), "x"))
a6 = int(sub6, 16)

# Skips bytes 19-21 and reades bytes 22 and 23
bi = os.read(3)
bi = os.read(2)
sub7 = str("{0:0>2}".format(ord(bi[1]), "x")) + str("{0:0>2}".format(ord(bi[0]), "x"))
a7 = int(sub7)

print "1. 512"
print "2. " + str(a2)
print "3. " + str(a3)
print "4. " + str(a4)
print "5. " + str(a5)
print "6. " + str(a6)
print "7. " + str(a7)
print "8. " + str(a2 * a3 * a4)
print "9. " + str(a2 * a7 + (a2 * a3 * a4))
print "10." + str(a2 * a7 * 2 + (a2 * a3 * a4))
print "11." + str(32 * a6 + (a2 * a7 * 2 + (a2 * a3 * a4)))
print "12." + str(((a7 * a2)/2) * a3 * a2 )

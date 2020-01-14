import base64
import codecs
import binascii
import hashlib

# Converting base64 to a hex string and saving it to a file
corruptedFile = open("corrupted.docx", "rb")
hexlify = codecs.getencoder('hex')
hexString = hexlify(base64.standard_b64decode(corruptedFile.read()))
decoded = open("decodedHex.txt", "w")
decoded.write(str(hexString))
decoded.close()

# Function that extracts files from the hex string and saving them correctly (help from github)
def carve(header, footer, output):
    with open("decodedHex.txt", 'r') as f:
        data = f.read()
        header_index = data.find(header, 0)
        footer_index = data.find(footer, 0)
        if header_index >= 0 and footer_index >= header_index:
            body = header + data[header_index + len(header): footer_index] + footer
            while body is not None:
                f = open(output,"w")
                f.write(str(body))
                f.close()

                # Finds the beginning and ends of files and adds them to the file. 
                header_index = data.find(header,footer_index + len(footer))
                footer_index = data.find(footer,footer_index + len(footer) + len(header))
                if header_index >= 0 and footer_index >= header_index:
                    body = header + data[header_index + len(header): footer_index] + footer
                else:
                    body = None
                    
    # Returns extracted hex file as output
    with open(output, 'rb') as g:
        content = g.read()
    output1 = binascii.unhexlify(content)
    g = open(output, 'wb')
    g.write(output1)
    g.close()
    
#Calling extract function
carve("ffd8", "ffd9", "jpgFile.jpg")
carve("255044462d312e", "2525454f460a", "pdfFile.pdf")
carve("89504e470d0a1a0a", "49454e44ae426082", "pngFile.png")
carve("474946383961", "00003b", "gifFile.gif")
carve("504b0304", "504b0506", "docxFile.docx")




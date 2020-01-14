from PIL import Image

def ExtractMessage(picture, output, index):
    # Opens the input file to inspect it
    secimg = Image.open(picture)
    # Gets the Size of the image and sets them to variables
    width, height = secimg.size
    # Creates the sting that the binary will fill into
    binarystr = ""

    # Loops through every byte by the height and then by the width of the picture
    for h in range(height):
        for w in range(width):
            # Gets all the pixels in the image
            pix = secimg.getpixel((w,h))
            # Gets the index of the color specified (R = 2, B = 1, G = 0) and
            # takes that byte to see if it can be anded to 1 and if the output
            # is false it adds a 0 to the sting of binary, else 1. 
            if pix[index] & 1 == 0:
                binarystr = binarystr + '0'
            else:
                binarystr = binarystr + '1'

    # sets the string for the final statement
    words = ""
    # continues loop until the end of the string
    while binarystr != "":
        # sets variable to the first 7 digits
        eight = binarystr[0:8]
        # re-defines b so that it no longer includes the first eight digits you read
        binarystr = binarystr[8:len(binarystr)]
        # changes the characters to binary
        int(eight, 2)
        # changes the binary number to a base 10 number then changes the number to a letter and saves it to a variable
        letter = chr(int(eight, 2))
        # Adds the letter to the string
        words += letter
        
    print "File " + output + " has been saved!"
    # creates a file that the output will be stored in.  
    file = open(output, "w")
    # writes the message into the files. 
    file.write(words)
    

ExtractMessage('confession01.png', 'test0.txt', 0)

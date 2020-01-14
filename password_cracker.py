import hashlib

def decoder(md5hash):
    # Reads the password file to begin to convert them to hashes. 
    passwords = open("passwords.txt", "r")
    # using a for loop, I iterate through all of the passwords to converts 
    # them to hex, source on sources 1-3 helped me build this function   
    for word in passwords:
        # strips the password of all spaces and new line characters
        pw = word.strip()
        # Turns the stripped word into a md5 hash
        hashes = hashlib.md5(pw).hexdigest()
        # Compares the md5 hash to the one inserted into the function
        # If the hashes match it returns the password to me 
        if hashes == md5hash:
            print "The password corresponding to " + md5hash + " is " + pw
            break

decoder("e076e7960533c2a998b91fa7c76fda2a")
decoder("37f2dbe5ec3f01f5f70b5ef61d37cdc5")
decoder("ae6e27cef852717bb3127bd0b6d2e6ef")

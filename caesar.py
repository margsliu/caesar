# Margaret Liu
# SoC Atlantis section
# PS: Crypto

from sys import argv, exit

from helpers import alphabet_position, rotate_character


# Function: encrypt(text,rot)
# Encrypts the text by rotating each character, except for non alphabeticals chars.
def encrypt(text,rot):
    if user_input_is_valid(argv) == False:
        print("usage: python3 caesar.py n")
        exit()
    else:
        text_new = ""
        for pos in range(len(text)):
            text_new += rotate_character(text[pos],int(rot))
        return text_new

def user_input_is_valid(cl_args):
    if (not cl_args[1].isdigit()) or (not len(cl_args) == 2):
        return False
    else:
        return True


#test = str(input("Type a message: "))
#print(encrypt(input("Type a message: "),int(argv[1])))
# or use
print(encrypt("Hello, World!",argv[1]))


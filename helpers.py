# Margaret Liu
# SoC Atlantis section
# PS: Crypto



# Function: alphabet_position
# which receives a letter (that is, a string with only one alphabetic character) and 
# returns the 0-based numerical position of that letter within the alphabet. 
# It should be case-insensitive.

def alphabet_position(letter):
	if (ord(letter) >= 97) and (ord(letter) <= 122): # lowercase
	    return ord(letter)-97
	elif (ord(letter) >= 65) and (ord(letter) <=90): # uppercase
		return ord(letter)-65
	else:
		pass


# Function: rotate_character
# rotates char by rot, to the right, and wraps around
# if non alphabetic, then return same input
def rotate_character(char,rot):
	if (ord(char) >= 97) and (ord(char) <= 122): # lowercase
		return chr(97+(alphabet_position(char)+rot)%26)
	elif (ord(char) >= 65) and (ord(char) <=90): # uppercase
		return chr(65+(alphabet_position(char)+rot)%26)
	else:
		return char
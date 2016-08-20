import webapp2
import cgi
from sys import argv, exit
#from helpers import alphabet_position, rotate_character
#from caesar import encrypt, user_input_is_valid

# HTML header and footer

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Formations: Caesar</title>
</head>
<body>
    <h1>Formations: Caesar</h1>
"""
page_footer = """
</body>
</html>
"""

# ============================================================

# Function: encrypt(text,rot)
# Encrypts the text by rotating each character, except for non alphabeticals chars.
def encrypt(text,rot):
    # if user_input_is_valid(argv) == False:
    #     #print("usage: python3 caesar.py n")
    #     #exit()
    #     pass
    #else:
        # text_new = ""
        # for pos in range(len(text)):
        #     text_new += rotate_character(text[pos],int(rot))
        # return text_new
    text_new = ""
    for pos in range(len(text)):
        text_new += rotate_character(text[pos],int(rot))
    return text_new
# def user_input_is_valid(userinput):
#     if (not userinput[1].isdigit()) or (not len(userinput) == 2):
#         return False
#     else:
#         return True

# Function: alphabet_position
# which receives a letter (that is, a string with only one alphabetic character) and
# returns the 0-based numerical position of that letter within the alphabet.
# It should be case-insensitive.

def alphabet_position(letter):
    if (ord(letter) >= 97) and (ord(letter) <= 122): # lowercase
        return ord(letter)-97
    elif (ord(letter) >= 65) and (ord(letter) <= 90): # uppercase
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

# ============================================================

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.formation-caesar.com
    """

    def get(self):

        form_instructions = "<h3>Encrypt something!</h3>"

        add_form = """
        <form action="/rot" method="post">
            <label>Rotate</label>
            <input type="text" size="80" name="to-be-encrypted"/>
            <label>by</label>
            <input type="number" size="10" name="rotation-amount"/>
            <label>letters</label>
            <input type="submit" value="Encrypt" style="margin-left:25px;">
        </form>

        """

        response = page_header + form_instructions + add_form + page_footer
        self.response.write(response)

class Rot(webapp2.RequestHandler):
    """ Handles requests coming in to /Rot
    """

    def post(self):

        to_be_encrypted = self.request.get("to-be-encrypted")
        rotation_amount = self.request.get("rotation-amount")
        encrypted_text = encrypt(to_be_encrypted, rotation_amount)

        form_instructions = "<h3>Encrypt something!</h3>"

        form_pt1 = """
        <form action="/rot" method="post">
            <label>Rotate</label>
            <input type="text" size="80" name="to-be-encrypted" value="
            """

        form_pt2 = """
        "/>
        <label>by</label>
        <input type="number" size="10" name="rotation-amount"/>
        <label>letters</label>
        <input type="submit" value="Encrypt" style="margin-left:25px;">
        </form>
        """

        add_form = form_pt1 + encrypted_text + form_pt2

        response = page_header + form_instructions + add_form + page_footer
        self.response.write(response)





app = webapp2.WSGIApplication([
    ('/', Index),
    ('/rot', Rot)
], debug=True)

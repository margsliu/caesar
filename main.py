import webapp2
import cgi

from helpers import alphabet_position, rotate_character
from caesar import encrypt, user_input_is_valid

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

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.formation-caesar.com
    """

    def get(self):

        form_instructions = "<h3>Enter some text to ROT13:</h3>"

        add_form = """
        <form action="/" method="post">
            <input type="text" size="80" name="to-be-encrypted"/>
            <input type="submit" value="Encrypt"/ style="margin-left:25px;">
        </form>

        """

        response = page_header + form_instructions + add_form + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)

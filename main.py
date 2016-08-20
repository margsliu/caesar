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



class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

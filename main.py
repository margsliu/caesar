import webapp2
import cgi

from helpers import alphabet_position, rotate_character
from caesar import encrypt, user_input_is_valid

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

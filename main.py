from google.appengine.ext import webapp
from services import handlers


app = webapp.WSGIApplication([('/', handlers.MainHandler)],
                             debug=True)


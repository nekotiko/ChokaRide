import simplejson
import logging
__author__ = 'bakeneko'

from google.appengine.ext import webapp

class MainHandler(webapp.RequestHandler):

    def get(self):
        self.response.out.write('Hello world!')

    def post(self):
        logging.warning ('[%r]', self.request.body)
        json = simplejson.loads(self.request.body)
        logging.warning (json)
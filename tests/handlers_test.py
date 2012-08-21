import simplejson

__author__ = 'bakeneko'

import unittest

import main
import webapp2

class MainHandler_Test (unittest.TestCase):

    def hello_world_test(self):
        ''' Testing Hello World! '''
        request = webapp2.Request.blank("/")

        response = request.get_response(main.app)

        self.assertEquals (response.status_int, 200)

    def test_json_test(self):
        ''' Just testing using JSON request
        '''

        request = webapp2.Request.blank("/")
        request.method = 'POST'

        json = {'name': 'test'}

        request.body = simplejson.dumps(json )

        response = request.get_response(main.app)

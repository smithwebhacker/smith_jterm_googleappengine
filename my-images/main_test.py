import unittest
import webapp2
import main

class TestHandlers(unittest.TestCase):
    def testMainpage(self):
        request = webapp2.Request.blank('/')
        

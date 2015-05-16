from image_count.example import Example
import unittest2

class TestExample(unittest2.TestCase):

	def test_do_this_does_that(self):		
		example = Example();
		self.assertEquals(example.do_this(), "bob");



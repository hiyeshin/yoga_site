"""
This file demonstrates writing tests using the unittest module.
THese will pass when we are running 'manage.py' test

Maybe later we'd better replace this with more appropriate tests
"""

from django.test import TestCase

class SimpleTest(TestCase):
	def test_basic_addition(self):
		self.assertEqual(1+1, 2)
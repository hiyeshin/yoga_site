"""
This file demonstrates writing tests using the unittest module. These will pass
when we manage to run manage.py
"""

from django.tests import TestCase

class SimpleTest(TestCase):
	def test_basic_addition(self):
		"""
		test test test
		"""
		self.assertEqual(1+1, 2)
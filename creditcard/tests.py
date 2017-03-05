#project-vcc/creditcard/test.py
# -*- coding: utf-8 -*-

from django.test import TestCase
from .models import CreditCard

class CreditCardTest(TestCase):
	"""
		docstring for CreditCardTest
	"""
	
	def get_number_valid(self):
		"""
			This method get a number starting with number four (VISA) and valid
		"""
		return 4916737331445694

	def get_number_starting_with_three(self):
		"""
			This method get a number starting with number six (AMERICAN EXPRESS)
		"""
		return 342169971301304

	def get_number_starting_with_five(self):
		"""
			This method get a number starting with number five (MASTERCARD)
		"""
		return 5285084794916154

	def get_number_starting_with_six(self):
		"""
			This method get a number starting with number six (DISCOVER)
		"""
		return 6011536275920491

	def create_credit_card(self, number):
		"""
			This method create a new credit card with one number
		"""
		number_creditcard = number
		CreditCard.objects.create(number=number_creditcard)

	def setUp(self):
		"""
			The setup for CreditCardTest
		"""
		self.create_credit_card(self.get_number_valid())
		self.create_credit_card(self.get_number_starting_with_five())
		self.create_credit_card(self.get_number_starting_with_six())

	def test_create_credit_card(self):
		"""
			This method test if you created one CreditCard with valid number
		"""
		number_creditcard = self.get_number_valid()
		creditcard_visa = CreditCard.objects.get(number=number_creditcard)
		self.assertEqual(number_creditcard, creditcard_visa.number)

	def test_data_create_is_not_none(self):
		"""
			This method verificy if the date_created property is populated when you create a new CreditCard
		"""
		number_creditcard = self.get_number_valid()
		creditcard_visa = CreditCard.objects.get(number=number_creditcard)
		self.assertNotEqual(None, creditcard_visa.number)

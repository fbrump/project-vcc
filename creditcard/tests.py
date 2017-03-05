#project-vcc/creditcard/test.py
# -*- coding: utf-8 -*-

from django.test import TestCase
from .models import CreditCard
from .validations import (
	validate_digit_start, 
	validate_digit_is_not_null,
	validate_number_digits
)

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
		return 374850035887914

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

	def get_number_with_less_digits(self):
		"""
			This method get a number starting with number six (DISCOVER)
		"""
		return 6011536275

	def get_number_with_more_digits(self):
		"""
			This method get a number starting with number six (DISCOVER)
		"""
		return 601153627592049148657

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

	def test_number_start_with_four(self):
		number_creditcard = self.get_number_valid()
		creditcard_visa = CreditCard.objects.get(number=number_creditcard)
		# Assert
		self.assertTrue(validate_digit_start(creditcard_visa))
		self.assertTrue(validate_digit_is_not_null(creditcard_visa))
		self.assertTrue(validate_number_digits(creditcard_visa))

	def test_number_start_with_five(self):
		number_creditcard = self.get_number_starting_with_five()
		creditcard_visa = CreditCard.objects.get(number=number_creditcard)
		# Assert
		self.assertTrue(validate_digit_start(creditcard_visa))
		self.assertTrue(validate_digit_is_not_null(creditcard_visa))
		self.assertTrue(validate_number_digits(creditcard_visa))

	def test_number_start_with_six(self):
		number_creditcard = self.get_number_starting_with_six()
		creditcard_visa = CreditCard.objects.get(number=number_creditcard)
		# Assert
		self.assertTrue(validate_digit_start(creditcard_visa))
		self.assertTrue(validate_digit_is_not_null(creditcard_visa))
		self.assertTrue(validate_number_digits(creditcard_visa))

	def test_number_start_with_three(self):
		number_creditcard = self.get_number_starting_with_three()
		creditcard_visa = CreditCard(number=number_creditcard)
		# Assert
		self.assertFalse(validate_digit_start(creditcard_visa))
		self.assertTrue(validate_digit_is_not_null(creditcard_visa))
		self.assertFalse(validate_number_digits(creditcard_visa))

	def test_number_is_not_null(self):
		creditcard_visa = CreditCard()
		self.assertFalse(validate_digit_is_not_null(creditcard_visa))

	def test_number_digits(self):
		number_creditcard = self.get_number_starting_with_five()
		creditcard_visa = CreditCard.objects.get(number=number_creditcard)
		self.assertTrue(validate_number_digits(creditcard_visa))

	def test_number_digits_with_more_digit(self):
		creditcard_visa = CreditCard(number=self.get_number_with_more_digits())
		self.assertFalse(validate_number_digits(creditcard_visa))

	def test_number_digits_with_less_digit(self):
		creditcard_visa = CreditCard(number=self.get_number_with_less_digits())
		self.assertFalse(validate_number_digits(creditcard_visa))




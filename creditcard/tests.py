#project-vcc/creditcard/test.py
# -*- coding: utf-8 -*-

from django.test import TestCase
from .models import CreditCard
from .validations import (
	validate_digit_start, 
	validate_digit_is_not_null,
	validate_number_digits,
	validate_digits_are_number,
	validate_consecutive_repeated,
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
		"""
			This method verificy if the credit card number is satrting with digit four
		"""
		number_creditcard = self.get_number_valid()
		creditcard_visa = CreditCard.objects.get(number=number_creditcard)
		# Assert
		self.assertTrue(validate_digit_start(creditcard_visa.number))
		self.assertTrue(validate_digit_is_not_null(creditcard_visa.number))
		self.assertTrue(validate_number_digits(creditcard_visa.number))

	def test_number_start_with_five(self):
		"""
			This method verificy if the credit card number is satrting with digit five
		"""
		number_creditcard = self.get_number_starting_with_five()
		creditcard_visa = CreditCard.objects.get(number=number_creditcard)
		# Assert
		self.assertTrue(validate_digit_start(creditcard_visa.number))
		self.assertTrue(validate_digit_is_not_null(creditcard_visa.number))
		self.assertTrue(validate_number_digits(creditcard_visa.number))

	def test_number_start_with_six(self):
		"""
			This method verificy if the credit card number is satrting with digit six
		"""
		number_creditcard = self.get_number_starting_with_six()
		creditcard_visa = CreditCard.objects.get(number=number_creditcard)
		# Assert
		self.assertTrue(validate_digit_start(creditcard_visa.number))
		self.assertTrue(validate_digit_is_not_null(creditcard_visa.number))
		self.assertTrue(validate_number_digits(creditcard_visa.number))

	def test_number_start_with_three(self):
		"""
			This method verificy if the credit card number is satrting with digit three
		"""
		number_creditcard = self.get_number_starting_with_three()
		creditcard_visa = CreditCard(number=number_creditcard)
		# Assert
		self.assertFalse(validate_digit_start(creditcard_visa.number))
		self.assertTrue(validate_digit_is_not_null(creditcard_visa.number))
		self.assertFalse(validate_number_digits(creditcard_visa.number))

	def test_number_is_not_null(self):
		"""
			This method verificy if the credit card number is not None or have value
		"""
		creditcard_visa = CreditCard()
		self.assertFalse(validate_digit_is_not_null(creditcard_visa.number))

	def test_number_digits(self):
		"""
			This method verificy if the credit card number have exactly 16 digits
		"""
		number_creditcard = self.get_number_starting_with_five()
		creditcard_visa = CreditCard.objects.get(number=number_creditcard)
		self.assertTrue(validate_number_digits(creditcard_visa))

	def test_number_digits_with_more_digit(self):
		"""
			This method verificy if the credit card number have exactly 16 digits is not True
		"""
		creditcard_visa = CreditCard(number=self.get_number_with_more_digits())
		self.assertFalse(validate_number_digits(creditcard_visa))

	def test_number_digits_with_less_digit(self):
		"""
			This method verificy if the credit card number have exactly 16 digits is not True
		"""
		creditcard_visa = CreditCard(number=self.get_number_with_less_digits())
		self.assertFalse(validate_number_digits(creditcard_visa))

	def test_digit_is_all_number(self):
		digits = self.get_number_valid()
		self.assertTrue(validate_digits_are_number(digits))

	def test_digit_is_all_number_digits_with_char(self):
		digits = 'assdf5788965487'
		self.assertFalse(validate_digits_are_number(digits))

	def test_digit_with_three_consecutive_repeated(self):
		digits = '4424424424442444'
		self.assertTrue(validate_consecutive_repeated(digits))

	def test_digit_with_four_consecutive_repeated(self):
		digits = '4424444424442444'
		self.assertFalse(validate_consecutive_repeated(digits))

	def test_digit_is_all_number_and_have_hyphen_or_not(self):
		digits = '5122-2368-7954 - 3214'
		self.assertFalse(validate_digits_are_number(digits))

		digits = '5122-2368-7954-3214'
		self.assertFalse(validate_digits_are_number(digits))

	def test_digit_have_just_numbers(self):
		digits = self.get_number_starting_with_six()
		self.assertTrue(validate_digits_are_number(digits))

	def test_digit_have_group_numbers_4_by_4(self):
		digits = '5122-236879543214'
		self.assertFalse(validate_digits_are_number(digits))

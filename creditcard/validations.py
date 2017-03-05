#project-vcc/creditcard/test.py
# -*- coding: utf-8 -*-

import re
from .models import CreditCard

def validate_digit_start(creditCard):
	"""
		This method verifica if the number of the credit card start with some digit validates.
	"""
	if (validate_digit_is_not_null(creditCard)):
		if (validate_starting_with(creditCard.number, 4) or
			validate_starting_with(creditCard.number, 5) or
			validate_starting_with(creditCard.number, 6)):
			return True
	return False

def validate_digit_is_not_null(creditCard):
	"""
		This method verifica if the number have any value.
	"""
	if (creditCard.number):
		return True
	return False

def validate_number_digits(creditCard):
	number = str(creditCard.number)
	if (len(number) == 16):
		return True
	return False

def validate_digits_are_number(digits):
	result = re.findall(r'^-?[0-9]+$', str(digits))
	if len(result) > 0:
		return True
	return False

def validate_starting_with(number, digit):
	"""
		This method verifica if the number start with digit.
	"""
	_number = str(number)
	return _number.startswith(str(digit))
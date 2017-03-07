#project-vcc/creditcard/test.py
# -*- coding: utf-8 -*-

import re
from .models import CreditCard

def validate_digit_start(digits):
	"""
		This method verifica if the number of the credit card start with some digit validates.
	"""
	if (validate_digit_is_not_null(digits)):
		number = digits
		if (validate_starting_with(number, 4)):
			return True
		if(validate_starting_with(number, 5)):
			return True
		if(validate_starting_with(number, 6)):
			return True	
	return False

def validate_digit_is_not_null(digits):
	"""
		This method verifica if the number have any value.
	"""
	if (digits):
		return True
	return False

def validate_number_digits(digits):
	number = get_just_numbers_typed(digits) #str(digits)
	if (len(number) == 16):
		return True
	return False

def validate_digits_are_number(digits):
	result = re.findall(r'^-?[0-9]+$', str(digits))
	if len(result) > 0:
		return True
	return False

def validate_digits_are_just_number(digits):
	result = re.findall(r'^[0-9]+$', str(digits))
	if len(result) > 0:
		return True
	return False

def validate_consecutive_repeated(digits):
	number = get_just_numbers_typed(digits) #str(digits)
	count = 0
	old_digit = None
	for digit in number:
		if (old_digit == digit):
			count = count + 1
			if (count > 3):
				return False
		else:
			count = 0
			old_digit = digit
	return True

def validate_starting_with(number, digit):
	"""
		This method verifica if the number start with digit.
	"""
	_number = str(number)
	return _number.startswith(str(digit))

def get_just_numbers_typed(digits):
	arr_numbers = re.findall('\d+', digits)
	return ''.join(arr_numbers)
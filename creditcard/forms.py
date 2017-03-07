#project-vcc/creditcard/forms.py
# -*- coding: utf-8 -*-

from django import forms
from .models import CreditCard
from .validations import (
	validate_consecutive_repeated,
	validate_digits_are_number,
	validate_digits_are_just_number,
	validate_number_digits,
	validate_digit_is_not_null,
	validate_digit_start,
	)

class CreditCardForm(forms.Form):
	"""
		This class mapping fields of the form
	"""
	def is_valid(self):
		valid = True
		
		_number = self.data['number']

		if (not validate_digit_is_not_null(_number)):
			self.add_errors("Can't working with NULL number → Invalid")
			valid=False
		if (not validate_consecutive_repeated(_number)):
			self.add_errors('It must NOT have 4 or more consecutive repeated digits.')
			valid=False
		if (not validate_digit_start(_number)):
			self.add_errors("Doesn't start with 4, 5 or 6 → Invalid")
			valid=False
		if (not validate_digits_are_just_number(_number)):
			if (validate_digits_are_number(_number)):
				self.add_errors("Separators other than '-' are used → Invalid")
				self.add_errors("Contains non digit characters → Invalid")
				valid=False
		if (not validate_number_digits(_number)):
		 	self.add_errors("%d digits in card number → Invalid" % (len(_number)))
		 	valid=False

		return valid
	def add_errors(self, message):
		self.add_error(None, message)
	def clean(self):
		cleaned_data = super(CreditCardForm, self).clean()

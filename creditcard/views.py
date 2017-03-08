#project-vcc/creditcard/views.py
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from .models import CreditCard
from .forms import CreditCardForm
from .validations import get_just_numbers_typed

import codecs
import os
import StringIO

def creditcard_list(request):
	"""
		This method return the list of the all creditcards for show.
	"""
	cards = CreditCard.objects.all()
	return render(request, 'creditcard/index.html', { 'cards': cards})

def creditcard_detail(request, id):
	"""
		This method return the details of the creditcard for show.
	"""
	card = CreditCard.objects.get(id=id)
	return render(request, 'creditcard/detail.html', { 'card': card})

def creditcard_create(request):
	"""
		This method return the details of the creditcard for show.
	"""
	messanges = []
	if (request.method == 'POST'):
		print(request.FILES)
		for file in request.FILES:
			print('entre file ==')
			print(file)
			_data = request.FILES['numbers'].read()
			print('data ====')
			print(_data)
			print('Other test')
			_data
		_form = CreditCardForm(data=request.POST, files=request.FILES)
		if (_form.is_valid()):
			print('form is valid')
			_number = get_just_numbers_typed(_form.data['number'])
			messanges.append('IS VALID!')
		else:
			print('form is not valid')
			messanges = _form.non_field_errors()
	return render(request, 'creditcard/create.html', { 'messanges': messanges })
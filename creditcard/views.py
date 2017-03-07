#project-vcc/creditcard/views.py
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import CreditCard
from .forms import CreditCardForm
from .validations import get_just_numbers_typed

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
		_form = CreditCardForm(data=request.POST, files=request.FILES)
		try:
			if (_form.is_valid()):
				print('form is valid')
				_number = get_just_numbers_typed(_form.data['number'])
				_creditCard = CreditCard.objects.create(number=int(_number))
				_creditCard.save()
				creditcard_list(request)
			else:
				print('form is not valid')
				messanges = _form.non_field_errors()
		except Exception as e:
			print(e)
			messanges.append(str(e))
	return render(request, 'creditcard/create.html', { 'messanges': messanges })
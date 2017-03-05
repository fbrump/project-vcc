#project-vcc/creditcard/views.py
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import CreditCard

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
	return render(request, 'creditcard/create.html')
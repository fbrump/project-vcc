#project-vcc/creditcard/views.py
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import CreditCard

def creditcard_list(request):
	"""
	"""
	cards = CreditCard.objects.all()
	return render(request, 'creditcard/list.html', { 'cards': cards})

def creditcard_detail(request, id):
	"""
	"""
	card = CreditCard.objects.get(id=id)
	return render(request, 'creditcard/list.html', { 'card': card})
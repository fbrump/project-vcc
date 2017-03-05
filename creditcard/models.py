#project-vcc/creditcard/models.py
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator

class CreditCard(models.Model):
	"""
		docstring for CreditCard

	"""
	number = models.IntegerField(validators=[MaxValueValidator(9999999999999999)])
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "CreditCard"
		verbose_name_plural = "CreditCards"

	def __str__(self):
		return '%s' % (self.number)
	def __unicode__(self):
		return '%s' % (self.number)

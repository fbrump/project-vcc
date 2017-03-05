#project-vcc/creditcard/models.py
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class CreditCard(models.Model):
	"""
		docstring for CreditCard
		
	"""
	number = models.IntegerField(max_length=16)
	date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "CreditCard"
        verbose_name_plural = "CreditCards"

    def __str__(self):
        return '%s' % (self.number)
    

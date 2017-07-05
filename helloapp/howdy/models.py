# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

""" user info"""
class Dreamreal(models.Model):
	website = models.CharField(max_length = 50)
	mail = models.CharField(max_length = 50)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	date =models.DateTimeField()
class Meta:
	db_table = "dreamrel" 

#class Choice(models.Model):
#	dreamreal = models.ForeignKey(Dreamreal, on_delete=models.CASCADE)

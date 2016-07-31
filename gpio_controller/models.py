from __future__ import unicode_literals

from django.db import models

# Create your models here.

class GPIOController(models.Model):
	name = models.CharField(max_length=200)
	pin = models.IntegerField()
	STATUS_CHOICES = ('ON', 'OFF')
	status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='OFF')
	desc = models.TextField(default='')
	action = models.CharField(max_length=200, default='')
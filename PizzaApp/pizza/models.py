import datetime

from django.db import models
from django.utils import timezone
class pizza(models.Model):
	pizza_name = models.CharField(max_length=200)
	pizza_ID = models.CharField(max_length=200)
	pizza_topping = models.CharField(max_length=200)
	def __str__(self):
		return self.pizza_name
	

class topping(models.Model):
	topping_name = models.CharField(max_length=200)
	topping_ID = models.CharField(max_length=200)
	def __str__(self):
		return self.topping_ID + " - " + self.topping_name

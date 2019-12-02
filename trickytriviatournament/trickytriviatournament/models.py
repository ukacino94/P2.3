"""

"""

from django.db import models

class Question(models.Model):
	"""
	Models a single question that the user gets asked along
	with all the information required to determine if the
	answer given by the user is correct.
	"""
	category = models.CharField(max_length=200)
	question = models.CharField(max_length=200)
	choice1 = models.CharField(max_length=200)
	choice2 = models.CharField(max_length=200)
	choice3 = models.CharField(max_length=200)
	choice4 = models.CharField(max_length=200)
	answer = models.CharField(max_length=200)

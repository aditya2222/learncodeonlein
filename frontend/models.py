from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=120)
	question = models.CharField(max_length=120)
	description = models.TextField(blank=True,null=True)
	java_code = models.TextField(blank=True,null=True)
	c_code = models.TextField(blank=True,null=True)

	def get_absolute_url(self):
		return reverse("index")


	def __str__(self):
		return self.title

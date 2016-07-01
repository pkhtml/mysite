from __future__ import unicode_literals

from django.db import models

# Create your models here.


class url_db(models.Model):
	url = models.CharField(max_length=500)
	title = models.CharField(max_length=200,blank=True, null=True)
	add_time = models.CharField(max_length=20)
	user = models.CharField(max_length=10)
	view_time = models.CharField(max_length=20,blank=True, null=True)
	view_count = models.IntegerField()
	urltype = models.IntegerField()


class type_db(models.Model):
	urltype = models.IntegerField()
	type_name = models.CharField(max_length=10)
	user = models.CharField(max_length=10)
 

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Video(models.Model):
	url = models.CharField(primary_key=True, max_length=100)
	transcript = models.TextField(max_length=90000) ##TODO for list
	pub_date = models.DateTimeField('date added to DB')

	def __str__(self):
		return self.video_url
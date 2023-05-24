from django.db import models

class Song(models.Model):
	name = models.CharField(max_length=150)
	length = models.IntegerField(default=0)

	def __str__(self):
		return self.name	

from django.db import models

class Author(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)

	def	__str__(self):
		return "%s %s" % (self.first_name, self.last_name)

class Book(models.Model):
	name = models.CharField(max_length=100)
	review = models.TextField(blank=True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
	
	def __str__(self):
		return self.name
		

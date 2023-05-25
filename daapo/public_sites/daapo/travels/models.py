from django.db import models

class Traveller(models.Model):
	first_name = models.CharField(max_length=160)
	last_name = models.CharField(max_length=160)
	email = models.EmailField(blank=True, null=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

class Destination(models.Model):
	name = models.CharField(max_length=160)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

class Trip(models.Model):
	name = models.CharField(max_length=200, blank=True)
	description = models.TextField(blank=True)
	cost = models.FloatField(blank=True, null=True)
	traveller = models.ForeignKey(Traveller, on_delete=models.CASCADE)
	destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.traveller} to {self.destination}'

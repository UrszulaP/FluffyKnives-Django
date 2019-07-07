from django.db import models
from django.contrib.auth.models import User # importuje wbudowaną tabelę User

class Item(models.Model):
	# id = models.AutoField(primary_key=True) - jest dodawane automatycznie przez Django
	itemName = models.CharField(max_length=30) # domyślnie blank=False - NOT NULL
	itemMainDescription = models.TextField(max_length=100, blank=True)
	itemPointsDescription = models.TextField(max_length=200, blank=True)
	itemImage = models.CharField(max_length=30)
	itemImage = models.ImageField(upload_to='items_pics')
	itemPrice = models.FloatField()

	def __str__(self):
		return self.itemName
from django.db import models
from django.contrib.auth.models import User # importuje wbudowaną tabelę User

class Item(models.Model):
    # id = models.AutoField(primary_key=True) - jest dodawane automatycznie przez Django
    item_name = models.CharField(max_length=30) # domyślnie blank=False - NOT NULL
    item_main_description = models.TextField(max_length=100, blank=True)
    item_points_description = models.TextField(max_length=200, blank=True)
    item_image = models.CharField(max_length=30)
    item_image = models.ImageField(upload_to='items_pics')
    item_price = models.FloatField()

    def __str__(self):
        return self.itemName
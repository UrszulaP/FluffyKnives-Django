from django.contrib import admin
from .models import Item

# adding Item model to the admin panel
admin.site.register(Item)
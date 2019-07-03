from django.contrib import admin
from .models import Profile

# adding Profile model to the admin panel
admin.site.register(Profile)
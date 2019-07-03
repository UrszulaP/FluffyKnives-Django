from django.db import models
from django.contrib.auth.models import User # built-in User model

# Profile model created to provide picture for user (User model doesn`t contain it)
class Profile(models.Model):
	# association to User
	user = models.OneToOneField(User, on_delete=models.CASCADE) # on_delete=models.CASCADE - User deleted -> Picture deleted, Picture deleted -> User not deleted
	image = models.ImageField(default='defaultpp.jpg', upload_to='profile_pics') # pip install Pillow needed; auto hashing names

	def __str__(self):
		return f'{self.user.username} Profile'

from django.db import models
from django.contrib.auth.models import User # built-in User model
from PIL import Image

# Profile model created to provide picture for user (User model doesn`t contain it)
class Profile(models.Model):
	# association to User
	user = models.OneToOneField(User, on_delete=models.CASCADE) # on_delete=models.CASCADE - User deleted -> Picture deleted, Picture deleted -> User not deleted
	image = models.ImageField(default='defaultpp.jpg', upload_to='profile_pics') # pip install Pillow needed; auto hashing names
	adress = models.CharField(max_length=200, blank=True)
	phone = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return f'{self.user.username} Profile'

	# resizing picture; overwriting built-in method that gets run after an instance of model is saved (also uploaded)
	def save(self):
		super().save()
		img = Image.open(self.image.path) # opens image of current instance
		if img.height > 125 or img.width > 125:
			outputSize = (125, 125)
			img.thumbnail(outputSize)
			img.save(self.image.path)

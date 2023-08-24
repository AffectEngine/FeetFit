from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
	# Add custom fields here
	profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
	date_of_birth = models.DateField(null=True, blank=True)
	phone_number = models.CharField(max_length=15, blank=True)
	address = models.TextField(blank=True)

	# Add any additional fields or methods you need

	def __str__(self):
		return self.username

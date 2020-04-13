from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # Create one-to-one mapping with User class
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    # When printing a model, we'll return the username
    def __str__(self):
        return self.user.username

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # Create one-to-one mapping with User class
    user = models.OnetoOneField(User)
    # Additional fields
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload="profile_pics", blank=True)

    # When printing a model, we'll return the username
    def __str__(self):
        return self.user.username

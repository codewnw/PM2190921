from django.db import models
from django.contrib.auth.admin import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(blank=True, upload_to = 'profile_pics')

    def __str__(self):
        return self.user.username
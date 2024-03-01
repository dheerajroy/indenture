from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='assets/profile_pictures/', blank=True)
    phone_no = models.CharField(max_length=15)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user} | {self.name} | {self.email}'

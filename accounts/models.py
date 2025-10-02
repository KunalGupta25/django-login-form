from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPE_CHOICES = [
    ('Patient', 'Patient'),
    ('Doctor', 'Doctor'),
]

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

from datetime import date, datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)


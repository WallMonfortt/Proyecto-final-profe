
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    cellphone = models.CharField(max_length=10)
    is_admin = models.BooleanField(default=False)
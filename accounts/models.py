from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User For Auth: You Can Add Custom Fields
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)

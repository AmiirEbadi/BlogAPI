from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

CHOICES = (
    ("writer" , "Writer"),
    ("normal" , "Normal")
)


class User(AbstractUser):
    Position = models.CharField(
        max_length=20,
        choices=CHOICES
    )
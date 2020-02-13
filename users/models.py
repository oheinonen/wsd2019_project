from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

usertypes = (
    ("dev", "developer"),
    ("player", "player")
)


class CustomUser(AbstractUser):
    usertype = models.CharField(max_length=10)
    games = models.ManyToManyField('gamestore.Game')
    test = models.CharField(max_length=10, choices=usertypes)

    def __str__(self):
        return self.username

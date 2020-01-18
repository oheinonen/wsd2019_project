from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=255, primary_key=True, unique=True)
    url = models.URLField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)

class Highscore(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    score = models.IntegerField()

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    price = models.IntegerField()
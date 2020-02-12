from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=255, primary_key=True, unique=True)
    url = models.URLField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    developer = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True)
    is_bought = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game:detail', kwargs={'pk': self.pk})


class GameSession(models.Model):
    id = models.AutoField(primary_key=True)
    #time = models.DateTimeField(auto_now = True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    gameState = models.TextField(max_length=1000)

    def __str__(self):
        return self.player.username + ': ' + self.game.name


class Highscore(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return self.player.username + ": " + str(self.score)

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now = True)
    # price = models.FloatField()

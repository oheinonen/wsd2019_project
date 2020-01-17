from django.db import models

# Create your models here.

class Developer(models.Model):
    name = models.CharField(max_length=12, primary_key=True, unique=True)
    password = models.CharField(max_length=50)
    usertype = models.CharField(max_length=10)

class Game(models.Model):
    name = models.CharField(max_length=255, primary_key=True, unique=True)
    url = models.URLField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    owner = models.ForeignKey(Developer, on_delete=models.CASCADE)

class Player(models.Model):
    name = models.CharField(max_length=12, primary_key=True, unique=True)
    password = models.CharField(max_length=50)
    usertype = models.CharField(max_length=10)
    games = models.ManyToManyField(Game)

class Highscore(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField()

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    price = models.IntegerField()

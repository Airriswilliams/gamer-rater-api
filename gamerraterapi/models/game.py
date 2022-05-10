from unicodedata import category
from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=1000)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    recommended_age = models.IntegerField()
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    category = models.ManyToManyField("Category", related_name="categories")
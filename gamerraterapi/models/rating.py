from django.db import models

class Rating(models.Model):
    rating_number = models.IntegerField()
    player = models.ForeignKey("player", on_delete=models.CASCADE)
    game = models.ForeignKey("game", on_delete=models.CASCADE)
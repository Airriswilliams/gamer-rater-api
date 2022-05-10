from django.db import models

class Review(models.Model):
    game_review = models.CharField(max_length=1000)
    player = models.ForeignKey("player", on_delete=models.CASCADE)
    game = models.ForeignKey("game", on_delete=models.CASCADE)

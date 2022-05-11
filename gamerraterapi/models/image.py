from django.db import models

class Image(models.Model):
    # url = models.ImageField()
    player = models.ForeignKey("player", on_delete=models.CASCADE)
    game = models.ForeignKey("game", on_delete=models.CASCADE)

# leaderboard/models.py
from django.db import models

class LeaderboardEntry(models.Model):
    username = models.CharField(max_length=255)
    score = models.IntegerField()
    game_type = models.CharField(max_length=255)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} - {self.score}'

from django.db import models

from .person_model import Person


class Positions(models.TextChoices):
    FORWARD = 'Forward'
    MIDFIELDER = 'Midfielder'
    DEFENDER = 'Defender'
    GOALKEEPER = 'Goalkeeper'


class Player(Person):

    photo = models.CharField(max_length=1000)
    position = models.CharField(
        max_length=20,
        choices=Positions.choices
    )
    player_number = models.IntegerField()
    is_first_team = models.BooleanField()

    def __str__(self):
        return f'{self.name} {self.lastname} ({self.player_number})'

    class Meta:
        db_table = 'player'


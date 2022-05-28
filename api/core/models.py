from abc import ABC

from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    flag_image = models.CharField(max_length=250)
    shield_image = models.CharField(max_length=250)


class Person(ABC):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date = models.DateField()


class Positions(models.TextChoices):
    FORWARD = 'Forward'
    MIDFIELDER = 'Midfielder'
    DEFENDER = 'Defender'
    GOALKEEPER = 'Goalkeeper'


class Player(Person, models.Model):

    photo = models.CharField(max_length=100)
    position = models.CharField(
        max_length=20,
        choices=Positions.choices
    )
    player_number = models.IntegerField()
    is_first_team = models.BooleanField()


class RolTeamStaff(models.TextChoices):
    COACH = 'Coach'
    ASSISTANT = 'Assistant'
    PHYSICIAN = 'Physician'
    PHYSICAL_TRAINER = 'Physical Trainer'


class Staff(Person, models.Model):

    nationality = models.CharField(max_length=100)
    rol = models.CharField(max_length=100, choices=RolTeamStaff.choices)

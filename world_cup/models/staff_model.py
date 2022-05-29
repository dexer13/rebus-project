from django.db import models

from .person_model import Person


class RolTeamStaff(models.TextChoices):
    COACH = 'Coach'
    ASSISTANT = 'Assistant'
    PHYSICIAN = 'Physician'
    PHYSICAL_TRAINER = 'Physical Trainer'


class Staff(Person):

    nationality = models.CharField(max_length=100)
    rol = models.CharField(max_length=100, choices=RolTeamStaff.choices)

    class Meta:
        db_table = 'staff'

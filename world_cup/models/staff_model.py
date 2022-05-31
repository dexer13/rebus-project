from django.db import models

from . import Team
from .person_model import Person


class StaffManager(models.Manager):
    def get_oldest_coach(self):
        return self.filter(rol=RolTeamStaff.COACH.value).order_by('birth_date').first()


class RolTeamStaff(models.TextChoices):
    COACH = 'Coach'
    ASSISTANT = 'Assistant'
    PHYSICIAN = 'Physician'
    PHYSICAL_TRAINER = 'Physical Trainer'


class Staff(Person):

    nationality = models.CharField(max_length=100)
    rol = models.CharField(max_length=100, choices=RolTeamStaff.choices)
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='staff')

    objects = StaffManager()

    class Meta:
        db_table = 'staff'

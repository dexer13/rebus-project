from .meta_views import HealthAPIView
from .world_cup_views import (
    TeamsAPIView,
    TeamAPIView,
    PlayersAPIView,
    PlayerAPIView,
    StaffAPIView,
    StaffManyAPIView
)
from .resume_views import ResumeAPIView


__all__ = (
    'HealthAPIView',
    'TeamsAPIView',
    'TeamAPIView',
    'PlayersAPIView',
    'PlayerAPIView',
    'StaffAPIView',
    'StaffManyAPIView',
    'ResumeAPIView'
)

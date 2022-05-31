from rest_framework.urls import path

from .views import (
    HealthAPIView,
    TeamsAPIView,
    TeamAPIView,
    PlayersAPIView,
    PlayerAPIView,
    StaffManyAPIView,
    StaffAPIView,
    ResumeAPIView
)


urlpatterns = [
    path('health/', HealthAPIView.as_view()),

    path('api/v1/teams', TeamsAPIView.as_view()),
    path('api/v1/teams/<object_id>', TeamAPIView.as_view()),

    path('api/v1/players', PlayersAPIView.as_view()),
    path('api/v1/players/<object_id>', PlayerAPIView.as_view()),

    path('api/v1/staff', StaffManyAPIView.as_view()),
    path('api/v1/staff/<object_id>', StaffAPIView.as_view()),

    path('api/v1/resume', ResumeAPIView.as_view())
]

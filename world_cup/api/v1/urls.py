from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import re_path
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


schema_view = get_schema_view(
    openapi.Info(
        title="World Cup API",
        default_version='v1',
        description="Welcome to World Cup API",
        contact=openapi.Contact(email="deniseduardoisidrogonzalez@gmail.com")
    ),
    url='',
    public=True,
)

urlpatterns = [
    re_path(
        r'^api/v1/docs(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'api/v1/docs/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'api/v1/redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),

    path('health/', HealthAPIView.as_view()),

    path('api/v1/teams', TeamsAPIView.as_view()),
    path('api/v1/teams/<object_id>', TeamAPIView.as_view()),

    path('api/v1/players', PlayersAPIView.as_view()),
    path('api/v1/players/<object_id>', PlayerAPIView.as_view()),

    path('api/v1/staff', StaffManyAPIView.as_view()),
    path('api/v1/staff/<object_id>', StaffAPIView.as_view()),

    path('api/v1/resume', ResumeAPIView.as_view())
]

from rest_framework.urls import path

from .views.meta_views import HealthAPIView


urlpatterns = [
    path('health/', HealthAPIView.as_view()),
]

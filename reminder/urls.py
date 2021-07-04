from django.urls import path  # noqa:F401

from . import views  # noqa:F401

app_name = 'reminder'
urlpatterns = [
    path('', views.reminder, name='reminder')
]

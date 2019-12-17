from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log-hours', views.VolunteerLog, name='log_hours')
]
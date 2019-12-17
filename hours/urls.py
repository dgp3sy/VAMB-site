from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log-hours', views.HoursLogView.as_view(), name='log_hours')
]
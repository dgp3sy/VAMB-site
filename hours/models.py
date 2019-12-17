from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class VolunteerLog(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    computing_id = models.CharField(max_length=7)
    hours = models.IntegerField()
    honor = models.BooleanField(default=False)

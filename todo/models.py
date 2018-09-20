from django.db import models
from django.db.models.functions import datetime


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Todo(models.Model):
    tasks = models.CharField(max_length=70)
    period = models.IntegerField()
    time_of_accomplishing = models.DateTimeField(default=datetime.datetime.today())
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)




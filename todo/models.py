from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Todo(models.Model):
    tasks = models.CharField(max_length=70)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
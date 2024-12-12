from django.db import models

class IncrementValue(models.Model):
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Command(models.Model):
    command = models.CharField(max_length=100)
    executed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
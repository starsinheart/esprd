from django.db import models

class SensorData(models.Model):
    sensor_value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Command(models.Model):
    command = models.CharField(max_length=100)
    value = models.IntegerField()
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
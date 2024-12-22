from django.db import models

class SensorData(models.Model):
    sensor_value_1 = models.FloatField()
    sensor_value_2 = models.IntegerField()
    sensor_value_3 = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Command(models.Model):
    command = models.CharField(max_length=100)
    value = models.IntegerField()
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
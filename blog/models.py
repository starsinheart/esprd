from django.db import models

class SensorData(models.Model):
    sensor_value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
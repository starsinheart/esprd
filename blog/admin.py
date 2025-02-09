from django.contrib import admin
from .models import SensorData, Command

admin.site.register(SensorData)
admin.site.register(Command)
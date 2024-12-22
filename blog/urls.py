from django.urls import path
from . import views

urlpatterns = [
    path('send_command/', views.send_command, name='send_command'),
    path('get_commands/', views.get_commands, name='get_commands'),
    path('post_sensor_data/', views.post_sensor_data, name='post_sensor_data'),
    path('get_sensor_data/', views.get_sensor_data, name='get_sensor_data'),
    path('', views.interface, name='interface'),
]
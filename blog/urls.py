from django.urls import path
from . import views

urlpatterns = [
    path('post_data/', views.post_data, name='post_data'),
    path('get_data/', views.get_data, name='get_data'),
    path('', views.interface, name='interface'),  # URL для отображения интерфейса
]
from django.urls import path
from .views import api_view, interface
from . import views

urlpatterns = [
    path('', views.interface, name='interface'),
    path('api/', views.api_view, name='api'),
]
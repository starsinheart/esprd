from django.urls import path
from . import views

urlpatterns = [
    path('blog/post_data/', views.post_data, name='post_data'),
    path('blog/get_data/', views.get_data, name='get_data'),
]
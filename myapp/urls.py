from django.urls import path
from .views import index, landing
urlpatterns = [
    path('landing/', landing, name='landing'),
    path('home/<str:pk>/',index, name='home'),
    
]

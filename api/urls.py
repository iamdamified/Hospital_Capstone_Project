from django.urls import path
from .views import HomePageApi

urlpatterns = [
    path('', HomePageApi, name='home')
]
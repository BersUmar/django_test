from django.urls import path

from dogs.apps import DogsConfig
from dogs.views import index, breed

app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('breed/', breed, name='breed'),
    ]

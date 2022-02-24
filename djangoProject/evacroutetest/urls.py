
from .views import index
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path(r'', index, name='index')
]
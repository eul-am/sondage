"""Ici, on associe la vue (views.py) aux URLs ci-dessous"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
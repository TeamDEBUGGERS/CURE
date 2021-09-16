from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('num', views.numpad),
    path('temp', views.temp)
]
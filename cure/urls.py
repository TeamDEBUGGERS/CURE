from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index),
    path('num', views.numpad),
    path('temp', views.temp),
    path('vein', views.vein),
    path('veincomplete', views.veincomplete),
    path('regi1', views.regikeypad1),
    path('regi2', views.regikeypad2),
    path('complete', views.tempcomplete)
]
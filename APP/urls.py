from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('index', index),
    path('SIGpage/<str:SIGname>', SIGpage),
    path('sidebar', sidebar),
]

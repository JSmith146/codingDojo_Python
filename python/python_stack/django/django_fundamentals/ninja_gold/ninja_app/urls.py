from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('reset', views.reset),
    path('gold', views.process_gold)
]
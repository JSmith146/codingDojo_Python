from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('reset',views.reset),
    path('plus_one',views.plus_one)
    # path('rand_word', views.rand_word)
]
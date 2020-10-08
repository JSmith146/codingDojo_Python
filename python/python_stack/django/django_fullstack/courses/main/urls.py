from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('courses', views.index),
    path('courses/create', views.create),
    path('courses/<int:id>/destroy', views.delete),
    path('courses/<int:id>/comments', views.comments),
    path('courses/<int:id>/comments/new', views.new_comment)
]

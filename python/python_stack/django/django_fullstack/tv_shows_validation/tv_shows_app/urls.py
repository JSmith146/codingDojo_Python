from django.urls import path, include
from . import views

urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.add_new_show),
    path('shows/create', views.create_new_show),
    path('shows/<int:id>', views.display_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/update', views.update_show),
    path('shows/<int:id>/destroy', views.delete_show)
]
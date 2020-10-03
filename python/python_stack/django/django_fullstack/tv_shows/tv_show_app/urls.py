from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('show/new', views.add_new_show),
    path('show/create', views.create_show),
    path('show/<int:id>', views.display_show),
    path('show/<int:id>/edit', views.edit_show),
    path('show/<int:id>/update', views.update_show),
    path('show/<int:id>/destroy', views.delete_show)
]
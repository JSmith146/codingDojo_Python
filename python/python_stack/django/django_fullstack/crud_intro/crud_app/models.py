from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
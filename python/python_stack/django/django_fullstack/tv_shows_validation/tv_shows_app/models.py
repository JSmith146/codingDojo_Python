from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['title'])==0 or len(postData['title'])<2:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) == 0 or len(postData['network']) <3:
            errors['network'] = "Network should be a least 3 characters"
        if len(postData['desc']) == 0 or len(postData['desc'])< 10:
            errors['desc'] = "Description should be a least 10 characters"
        if postData['release_date'] == '':
            errors['release_date'] = "Release Date is required"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255, unique=True)
    network = models.CharField(max_length = 255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) <5:
            errors['name'] = "Course name must be greater than 5 characters"
        if len(postData['desc']) <15:
            errors['desc'] = "Description must be greater than 15 characters"
        return errors

class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
    

class Course(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.OneToOneField(Description, related_name="course", on_delete=models.CASCADE)
    objects = CourseManager()

class Comment(models.Model):
    content = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, related_name="comments",on_delete=models.CASCADE)

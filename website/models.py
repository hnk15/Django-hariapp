from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    collage=models.CharField(max_length=200)
    age=models.IntegerField()
    is_active=models.BooleanField(default=False)
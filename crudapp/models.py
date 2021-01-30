from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=20)
    sub=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.CharField(max_length=12)

    def __str__(self):
        return self.name

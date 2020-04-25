from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    email = models.CharField(max_length=36)
    subject = models.CharField(max_length=9)


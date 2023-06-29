from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.CharField(max_length=10, default=0)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=300, default="")
    phone = models.CharField(max_length=10, default=0)
    course = models.CharField(max_length=300, default="")
    semester = models.IntegerField(default=1)
    language = models.CharField(max_length=50, default="", null=True, blank=True)



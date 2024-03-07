from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)


class Course(models.Model):
    title = models.CharField(max_length=100)

from django.db import models

# Create your models here.
class Student(models.Model):
    studentNo = models.IntegerField()
    studentName = models.CharField(max_length=50)
    studentClass = models.IntegerField()
    studentAddress = models.CharField(max_length=100)


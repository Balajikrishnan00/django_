from django.db import models


# Create your models here.
class Students(models.Model):
    studentID = models.CharField(max_length=10)
    studentName = models.CharField(max_length=30)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=30)
    studentState = models.CharField(max_length=30)


class StudentMarks(models.Model):
    mark1 = models.IntegerField()
    mark2 = models.IntegerField()
    mark3 = models.IntegerField()
    mark4 = models.IntegerField()
    mark5 = models.IntegerField()


class StudentGrades(models.Model):

    total = models.IntegerField()
    grade = models.CharField(max_length=1)
    result = models.CharField(max_length=1)

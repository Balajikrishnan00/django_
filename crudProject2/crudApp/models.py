from django.db import models


# Create your models here.
class Employee(models.Model):
    empID = models.IntegerField()
    empName = models.CharField(max_length=20)
    empSalary = models.IntegerField()

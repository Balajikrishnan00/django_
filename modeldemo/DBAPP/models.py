from django.db import models

# Create your models here.
class Employee(models.Model):

    empNo = models.IntegerField()
    empName = models.TextField()
    empSalary = models.IntegerField()
    empAddress = models.TextField()


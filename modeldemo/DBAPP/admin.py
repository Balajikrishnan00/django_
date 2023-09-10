from django.contrib import admin
from DBAPP.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    emp_details = ["EmpID","EmpName","EmpSalary","EmpAddress"]

admin.site.register(Employee,EmployeeAdmin)

from django.contrib import admin
from crudApp.models import Employee


# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    empList = ['empID', 'empName', 'empSalary']


admin.site.register(Employee, EmpAdmin)

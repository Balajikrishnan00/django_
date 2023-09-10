from django.contrib import admin
from CRUDApp.models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list1e = ['studentNo','studentName','studentClass1','studentAddress']

admin.site.register(Student, StudentAdmin)


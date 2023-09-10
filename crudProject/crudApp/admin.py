from django.contrib import admin
from crudApp.models import Students, StudentMarks, StudentGrades


# Register your models here.
class Student10thAdmin(admin.ModelAdmin):
    List = ['studentID', 'studentName', 'studentAge', 'studentCity', 'studentState']


class studentMarks(admin.ModelAdmin):
    markList = ['m1', 'm2', 'm3', 'm4,', 'm5']


class StudentGrade(admin.ModelAdmin):
    list = ['t', 'g', 'r']


admin.site.register(StudentGrades, StudentGrade)
admin.site.register(Students, Student10thAdmin)
admin.site.register(StudentMarks, studentMarks)

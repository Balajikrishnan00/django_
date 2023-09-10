from django import forms
from CRUDApp.forms import models,Student

class StudentForm(forms.ModelForm) :
    class Meta:
        model = Student
        field = '__all__'
    studentNo = models.IntegerField()
    studentName = models.CharField(max_length=50)
    studentClass = models.IntegerField()
    studentAddress = models.CharField(max_length=100)

    
   
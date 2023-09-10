from django.shortcuts import render
from CRUDApp.models import Student

# Create your views here.

def studentlistView(request):
    students = Student.objects.all()
    dict_view = {'students':students}
    return render(request,'crudapp/index.html',context=dict_view)



 
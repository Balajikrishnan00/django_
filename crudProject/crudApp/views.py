from django.shortcuts import render
from crudApp.forms import StudentForms
from crudApp.models import Students, StudentMarks


# Create your views here.

def studentResultView(request):
    List = StudentMarks.objects.all()
    studentsDict = {"list": List}
    return render(request, 'crudApp/index.html', context=studentsDict)


def addStudentView(request):
    form = StudentForms()
    return render(request, 'crudApp/create.html', {"Form": form})

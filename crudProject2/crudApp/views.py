from django.shortcuts import render, redirect
from crudApp.models import Employee
from crudApp.forms import EmpForms


# Create your views here.

def index(request):
    from_db = Employee.objects.all()
    dict_data = {"form": from_db}
    return render(request, "crudapp/index.html", context=dict_data)


def createView(request):
    form = EmpForms()
    if request.method == 'POST':
        form = EmpForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view')
    return render(request, 'crudapp/create.html', {"form": form})


def deleteView(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/view')


def updateView(request, id):
    emp_data = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmpForms(request.POST,instance=emp_data)
        if form.is_valid():
            form.save()
            return redirect('/view')
    return render(request, 'crudapp/update.html', {'emp_data': emp_data})

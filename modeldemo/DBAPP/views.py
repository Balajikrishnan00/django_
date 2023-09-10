from django.shortcuts import render
from django.http import HttpResponse
from DBAPP.models import Employee


# Create your views here.

def empDetail(req):
    emp_data = Employee.objects.all()
    print(emp_data)
    emp_dict = {"emp_list": emp_data}
    
    empDetails = {"ID":101,"EmpName":"Balaji","EmpSalary":20000,"EmpAddress":"Sivaganga"}
    return render(req, 'DBAPP/employee.html', context=emp_dict)

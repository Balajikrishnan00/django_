from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
def welcome(req):
    return HttpResponse("welcome")

def empDetailView(req):
    form = forms.EmployeeInfo()
    empInfo = {'form':form}
    return render(req , 'formApp/form.html',context=empInfo)
    
from django import forms


class EmployeeInfo(forms.Form):
    
    name = forms.CharField()
    salary = forms.IntegerField()
    
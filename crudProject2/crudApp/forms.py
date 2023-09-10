from django import forms
from crudApp.models import Employee


class EmpForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        print(fields)


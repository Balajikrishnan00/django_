from django import forms
from crudApp.models import Students


# create you forms here.
class StudentForms(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'


from django import forms
from crudApp.models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta: # inner class for models,not subclasses
        model = Employee
        fields = '__all__'
        # expect some field 
        # exclude =['fieldName']
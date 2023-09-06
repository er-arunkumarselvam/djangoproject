from django import forms

# Create your forms here
class StudentForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    

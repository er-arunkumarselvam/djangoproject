from django.shortcuts import render
from . import forms

# Create your views here.
def studentDataView(request):
    studentInfo=forms.StudentForm()
    studentDataInfo ={'form':studentInfo}
    return render(request,'formApp/studentDataView.html',context=studentDataInfo)
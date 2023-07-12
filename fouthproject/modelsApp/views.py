from django.shortcuts import render
from modelsApp.models import Employees

# Create your views here.
def models(request):
    emp_data = Employees.objects.all() # To get all data for the employee model
    emp_dict = {'emp_list':emp_data} # To create a dictionary in above data for sharing to html file
    return render(request, 'modelsApp/index.html',context = emp_dict) # context= dictionary datatype format send into html
from django.shortcuts import render
from crudApp.models import Employee
from crudApp.forms import EmployeeForm
# Create your views here.
def read_veiw(request):
    employee = Employee.objects.all() # get all the data from database
    return render(request, 'crudApp/index.html', {'employee': employee}) # {'employee':employee} is context of the data using like as dictionary
    
def create_view(request):
    form =EmployeeForm()
    if request.method =='POST':
        form.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'crudApp/register.html',{'form':form})
from django.shortcuts import render, redirect
from crudApp.models import Employee
from crudApp.forms import EmployeeForm
# Create your views here.
def read_veiw(request):
    employee = Employee.objects.all() # get all the data from database
    return render(request, 'crudApp/index.html', {'employee': employee}) # {'employee':employee} is context of the data using like as dictionary
    
def create_view(request):
    form =EmployeeForm()
    if request.method =='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/read')
    return render(request,'crudApp/register.html',{'form':form})


def delete_view(request, id): #id (primary key)
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/read')

def update_view(request, id): #id (primary key)
    employee = Employee.objects.get(id=id)
    if request.method =='POST':
        form=EmployeeForm(request.POST, instance= employee) # instance is old data object update
        if form.is_valid():
            form.save()
            return redirect('/read')
    return render(request, 'crudApp/update.html', {'employee': employee})

from django.contrib import admin
from crudApp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list=['name','age'] # list of employees variable
    
# Admin Register
admin.site.register(Employee,EmployeeAdmin)
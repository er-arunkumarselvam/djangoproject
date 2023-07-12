from django.db import models

# Create your models here.
class Employees(models.Model):
    empNo = models.IntegerField()
    empName = models.CharField(max_length=25)
    empRole = models.CharField(max_length=25)
    empSalary = models.IntegerField()

def __str__(self):
    return 'Employees details are showed. Employee Name :' + empName

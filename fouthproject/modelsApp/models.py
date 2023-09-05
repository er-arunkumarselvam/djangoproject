from django.db import models

# Create your models here.
class Employees(models.Model):  # (modals.Model) -> Inheritance concept is applied, models(parent). Model is represented by field (models column name or table column heading)
    empNo = models.IntegerField()
    empName = models.CharField(max_length=25)
    empRole = models.CharField(max_length=25)
    empSalary = models.IntegerField()

def __str__(self):
    return 'Employees details are showed. Employee Name :' + empName

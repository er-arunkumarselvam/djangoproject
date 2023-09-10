import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRUD_Operation.settings')

import django
django.setup()

from crudApp.models import *
from faker import Faker
from random import *

faker = Faker()

def empData(n):
    for i in range(n):
        fakeName = faker.name()
        fakeAge = randint(20,50)
        emp_record=Employee.objects.get_or_create(name= fakeName, age=fakeAge)

     
empData(10) 





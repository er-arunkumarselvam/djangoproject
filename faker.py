# Import the os module to work with environment variables
import os

# Set the Django settings module for the project (replace 'projectName' with your actual project name)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectName.settings')

# Import the Django module and configure it
import django
django.setup()

# Import the necessary models and libraries
from appName.models import *
from faker import Faker
from random import *

# Create an instance of the Faker library for generating fake data
faker = Faker()

# Define a function named 'functionName' that takes 'value' as an argument
def functioName(value):
    # Loop 'value' times to generate fake data and populate the database
    for i in range(value):
        # Generate a random name using Faker
        variableName = faker.name()
        # Generate a random ID between 10 and 99
        variableId = randint(10,99)
        # Generate a random city name as an address using Faker
        variableName = faker.city()
        
        # Use the 'get_or_create' method to either retrieve an existing record or create a new one
        # Replace 'className' with the actual name of your model class, 
        # and 'classVariableName' and 'classsVariableId' with the actual field names.
        record = className.objects.get_or_create(classVariableName= variableName, classsVariableId=variableId)



# Call the 'functionName' function to execute it      
functionName() 





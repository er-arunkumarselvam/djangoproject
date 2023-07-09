from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Business Logic
def welcome(request):
    message = '<h1>Welcome to Our First Project</h1>'
    return HttpResponse(message)
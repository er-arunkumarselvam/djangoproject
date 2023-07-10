from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def gm_view(request):
    return HttpResponse('<h1>Good Morning</h1>')

def ga_view(request):
    return HttpResponse('<h1>Good Afternoon</h1>')

def ge_view(request):
    return HttpResponse('<h1>Good Evening</h1>')
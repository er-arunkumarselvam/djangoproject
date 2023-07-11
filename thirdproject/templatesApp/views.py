from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.


def home(request):
    BASE_DIR2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('<h1>'+BASE_DIR2+'</h1>')
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    print('<h1>'+TEMPLATES_DIR+'</h1>')
    
    return render(request, 'index.html',{'Name': 'Arunkumar'})
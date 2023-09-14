from django.shortcuts import render
from django.views.generic import View, TemplateView 
from django.http import HttpResponse

# Create your views here.
class FirstClassView(View):
    def get(self, request): #instance Function self confirm 
        return HttpResponse('<h1>First Class</h1>')
    
class SecondClassView(TemplateView):
    template_name = 'ClassBasedView/class.html' # template name is  important to ClassBased Views 
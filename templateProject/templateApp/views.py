from django.shortcuts import render
import datetime
# Create your views here.
def display(request):
	# Template Tags
	date =datetime.datetime.now()
	date_dict={'display_date':date} # dictionary format compulsory
	return render(request, 'templateApp/index.html',context=date_dict)
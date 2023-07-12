from django.shortcuts import render
import datetime

def home(request):
    date = datetime.datetime.now()    
    hour =int(date.strftime("%H"))
    if hour<12:
        message= 'Good Morning'
    elif hour<16:
        message= 'Good Afternoon'
    elif hour<23:
         message= 'Good Evening'
    name = 'Arunkumar'
    date_dict={'diplay_date':date,'emp_name':name,'greeting_message':message}
    return render(request, 'index.html',context=date_dict)
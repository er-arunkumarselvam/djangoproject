from django.shortcuts import render

# Cookies count for Session ID
def cookies_count_view(request):
    count=request.session.get('count',0)       # request function session
    total= int(count)+1         
    request.session['count'] = total
    print(request.session.get_expiry_date())
    return render(request,'cookiesApp/cookies.html',{'count':total})





# Create your views here.
# find Cookies 
# def cookies_count_view(request):
#    count=request.COOKIES.get('count',0)       # dictionary
#    total= int(count)+1         
#    response = render(request,'cookiesApp/cookies.html',{'count':total})
#    response.set_cookie('count',total) # set_cookie function of response
#    return response
# response set cookies






    
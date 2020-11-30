from django.http import response
from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from login.models import Member
from home.models import Nodes

from login.forms import LoginForm,RegisterForm


# Create your views here.




# return Page if success
def success_login(request):
    
    if request.method == "POST":
        myloginform = LoginForm(request.POST)
        if myloginform.is_valid():
            email = myloginform.cleaned_data['email']
            password = myloginform.cleaned_data['password']
            
            try:
                user = Member.objects.get(email = email)
                
            except:
                
                user = None
                
            if (user and password == user.password):
                
                try:
                    mynode = Nodes.objects.filter(id_user = user.id )
                    
                except:
                    mynode = "None"
                    print("no element")
                
                
                response = render(request,"home/home.html",{"nodes":mynode,"username":user.username,'gender':user.gender})
                response.set_cookie('user', user)
                response.set_cookie('username', user.username)
                response.set_cookie('gender', user.gender)
                response.set_cookie('id_user', user.id)
                # print(user.password, user.id)
                return response
                
                
                # if 'user' in request.COOKIES:
                    # user = request.COOKIES['user']
                    # return render(request, 'myapp/home.html')
                    
            else:
                
                return render(request,"login/login.html", {"err" : "err"})
                
    return HttpResponse("error for form valedtion")





# success Register if Success
def success_register(request):

    if request.method == "POST":
        myregisterform = RegisterForm(request.POST)
        if myregisterform.is_valid():
            
            username = myregisterform.cleaned_data['username']
            email = myregisterform.cleaned_data["email"]
            password = myregisterform.cleaned_data['password']
            gender = myregisterform.cleaned_data['gender']
            
            try:
                user = Member.objects.get(email = email)
                
            except:
                
                user = None 
                
            if user:
                return render(request, "login/register.html", {"email_is_exist" : "email is exist"})
            
            else:
                
                mymembar = Member(
                    
                    username = username,
                    email = email,
                    password = password,
                    gender = gender
                )
                
                mymembar.save()
                
                return render(request, "login/login.html")
        return HttpResponse("error in valid")   
                
    
    return HttpResponse("error in register")





def logout(request):
    
    if request.method == "POST":
        
        response = render(request,"login/login.html")
        response.delete_cookie('user')
        response.delete_cookie('username')
        response.delete_cookie('gender')
        response.delete_cookie('id_user')
        # print(user.password, user.id)
        return response


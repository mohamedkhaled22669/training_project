from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpRequest
from themedia.models import Profile
from themedia.forms import FormsProfile


def Test_media_done(request):
    return render(request, "themedia/index.html")



def Test_media(request):
    
    if request.method == "POST":
        myform = FormsProfile(request.POST,request.FILES)
        myprofile = Profile()
        if myform.is_valid():
            myprofile.name = myform.cleaned_data["name"]
            myprofile.picture = myform.cleaned_data["picture"]
            myprofile.save()
            
            return render(request, "themedia/saved.html",{"myprofile" : myprofile})
        return HttpResponse("error in if valid")
    return HttpResponse("error in request post")
        

from django.shortcuts import redirect, render

from django.http import response

from django.http import HttpRequest,HttpResponse

from home.forms import AddNode, SendNode,UpdateNode,DeleteNode

from home.models import Nodes

from django.core.mail import send_mail
# Create your views here.

def home(request):
    
    if 'user' in request.COOKIES:
        id_user = request.COOKIES['id_user']
        username = request.COOKIES['username']
        gender = request.COOKIES['gender']
        try:
            mynode = Nodes.objects.filter(id_user = id_user )
            return render(request,"home/home.html",{"nodes":mynode,"username":username,'gender':gender})
        
        except:
            print("no element")
            return render(request,"home/home.html")
        
    
    return render(request,"login/login.html")
    

# def testhome(request):
    
#     return redirect("home")


def add_node(request):
    if 'user' in request.COOKIES:
        
        id_user = request.COOKIES['id_user']
        username = request.COOKIES['username']
        gender = request.COOKIES['gender']
        
        return render(request,"home/add.html",{"username":username,'gender':gender})
    
    return render(request,"login/login.html")
    



def add_node_success(request):
    if 'id_user' in request.COOKIES:
        id_user = request.COOKIES['id_user']
        if request.method == "POST":
            myaddnodeform = AddNode(request.POST)
            if myaddnodeform.is_valid():
                subject = myaddnodeform.cleaned_data['subject']
                content = myaddnodeform.cleaned_data['content']
                
                mynodes = Nodes(
                    subject = subject,
                    content = content,
                    id_user = id_user
                )
                
                mynodes.save()
                        
                id_user = request.COOKIES['id_user']
                username = request.COOKIES['username']
                gender = request.COOKIES['gender']
                try:
                    mynode = Nodes.objects.filter(id_user = id_user )
                    return render(request,"home/home.html",{"nodes":mynode,"username":username,'gender':gender, "add_success" : "add_success"})
                
                
                # Not important
                except:
                    print("no element")
                    return render(request,"home/home.html")
               
            return HttpResponse("error you are edit in browsr")
        return render(request,"login/login.html")
    return render(request,"login/login.html")





def delete_node(request):
    
    if request.method == "POST":
        mydeleteform = DeleteNode(request.POST)
        if mydeleteform.is_valid():
            id = mydeleteform.cleaned_data['id']
            
            try:
                del_obj = Nodes.objects.get(id = id)
            
            except:
                del_obj = None
            
            del_obj.delete()
            
            
            id_user = request.COOKIES['id_user']
            username = request.COOKIES['username']
            gender = request.COOKIES['gender']
            try:
                mynode = Nodes.objects.filter(id_user = id_user )
                return render(request,"home/home.html",{"nodes":mynode,"username":username,'gender':gender})
            
            except:
                print("no element")
                return render(request,"home/home.html")
        return render(request,"login/login.html")
    return render(request,"login/login.html")




def update_node(request):
    
    if request.method == "POST":
        myupdateform = UpdateNode(request.POST)
        if myupdateform.is_valid():
            id = myupdateform.cleaned_data['id']
            subject = myupdateform.cleaned_data['subject']
            content = myupdateform.cleaned_data['content']

            id_user = request.COOKIES['id_user']
            
            myupdate = Nodes(
                id = id,
                subject = subject,
                content = content,
                id_user = id_user,
            )
            
            myupdate.save()
            
            username = request.COOKIES['username']
            gender = request.COOKIES['gender']
            try:
                mynode = Nodes.objects.filter(id_user = id_user )
                return render(request,"home/home.html",{"nodes":mynode,"username":username,'gender':gender})
        
            except:
                return render(request,"login/login.html")
            
        print("error")
    return render(request,"login/login.html")
            
    


def send_node(request):
    if 'id_user' in request.COOKIES :
        if request.method == "POST":
            mysendnode = UpdateNode(request.POST)
            if mysendnode.is_valid():
                id = mysendnode.cleaned_data['id']
                subject = mysendnode.cleaned_data['subject']
                content = mysendnode.cleaned_data['content']

                id_user = request.COOKIES['id_user']
                
            
                username = request.COOKIES['username']
                gender = request.COOKIES['gender']
                
                return render(request,'home/send.html',{'id':id, 'subject':subject, 'content':content,'id_user':id_user,"username":username,'gender':gender })
              
            
            return render(request,"login/login.html")
        return render(request,"login/login.html")
            
    else:
        return render(request,"login/login.html")


def send_node_success(request):
    
    if request.method == "POST":
        mysendnode = SendNode(request.POST)
        if mysendnode.is_valid():
            id = mysendnode.cleaned_data['id']
            subject = mysendnode.cleaned_data['subject']
            content = mysendnode.cleaned_data['content']
            emails = mysendnode.cleaned_data['emails']
           
            
            mylistemail = emails.split()
            
            # print(mylistemail)
            id_user = request.COOKIES['id_user']
            user = request.COOKIES['user']
            
            myupdate = Nodes(
                id = id,
                subject = subject,
                content = content,
                id_user = id_user,
            )
            
            myupdate.save()
            
            send_mail(subject,content,user,mylistemail,fail_silently=True)
            
            username = request.COOKIES['username']
            gender = request.COOKIES['gender']
            try:
                mynode = Nodes.objects.filter(id_user = id_user )
                return render(request,"home/home.html",{"nodes":mynode,"username":username,'gender':gender,"send_success" : "send_success"})
            
            except:
                return HttpResponse("error ?")
    return render(request,"login/login.html")
                


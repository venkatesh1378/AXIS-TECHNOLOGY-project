from django.shortcuts import render,HttpResponse,redirect
from .forms import StudentForm,Studentlogin,adminlogin,UserTime
from.models import Student,usertimings
from django.contrib import messages
 
from django.contrib.auth.models import User

def Home(request):
    return render(request,'home.html')
def Registration(request):
    if request.method=='GET':
       a=StudentForm()
       return render(request,'registration.html',{'a':a})
    else:
        if request.method=="POST":
           a=StudentForm(request.POST)
           if a.is_valid():  
              a.save()
              messages.success(request,"<h1>you registred<h1>")               
        return render(request,'registration.html',{'a':a})



def login(request):
    if request.method=="GET":
        b=Studentlogin()
        return render(request,'login.html',{'b':b})
    else:
        if request.method=="POST":
            b=Studentlogin(request.POST)
            if b.is_valid():
                b.save()
        return redirect("/intern/userhome")     
def admin(request): 
    if request.method=='GET':
        c=adminlogin()
        return render(request,'admin.html',{'c':c})
    else:
        if request.method=='POST':
            c=adminlogin(request.POST)
            if  c.is_valid():
                usid=request.POST.get("username")
                passw=request.POST.get("password")
                if usid=="admin" and passw=="admin":
                    c.save()
                return render(request,'adminscreen.html')
def viewusers(request):
    context={"viewusers":Student.objects.all()}
    return render(request,'viewuserdetails.html',context)  
def userhomepage(request):
    if request.method=="GET":
       d=UserTime()
       return render(request,'userhomepage.html',{'d':d})
    else:
        if request.method=="POST":
            d=UserTime(request.POST)
            if d.is_valid():
                d.save()     
        return redirect('/intern/login')
def adminuser(request):
    context={"userTimings":usertimings.objects.all()}
    return render(request,'usertimingdetails.html',context)  
    
    
            
               
   
   
    

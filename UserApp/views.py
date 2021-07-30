from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from AdminApp.models import Category,Song
from UserApp.models import UserInfo

# Create your views here.

def home(request):
    cats = Category.objects.all()
    songs = Song.objects.all()
    return render(request,"home.html",{"cats":cats,"songs":songs})

def ShowSong(request,sid):
    cats = Category.objects.all()
    songs = Song.objects.filter(Category=sid)
    return render(request,"home.html",{"cats":cats,"songs":songs})

def PlaySong(request,sid):
    cats=Category.objects.all()
    song=Song.objects.get(id=sid)
    return render(request,"playsong.html",{"song":song,"cats":cats,"sid":sid})
  

def SignUp(request):
    if(request.method=="POST"):
        email = request.POST["email"]
        username = request.POST["uname"]
        password = request.POST["pwd"]
        if UserInfo.objects.filter(username=username).exists():
            return render(request,"SignUp.html",{"invalid":username+" already taken."})

        else:
            new_user=UserInfo()
            new_user.email=email
            new_user.username=username
            new_user.password=password
            new_user.save()
            return redirect(Login)
    else:
        request.session.clear()
        return render(request,"SignUp.html",{})

def Login(request):
    if(request.method=="GET"):
        return render(request,"Login.html",{})
    else:
        username = request.POST["uname"]
        password = request.POST["pwd"]
        try:
            
            new_user = UserInfo.objects.get(username=username,password=password)
            request.session["uname"]=username
        except:  
            pass
        return redirect(home) 

def Logout(request):
    request.session.clear()
    return redirect(home)               
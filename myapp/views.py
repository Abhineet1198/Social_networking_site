from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from .models import *


def home(request):
    try:
        user=User.objects.get(username=request.user)
        return HttpResponseRedirect('/profile/')
    except:
        if(request.method=='POST'):
            uname=request.POST.get('username')
            pward = request.POST.get('password')
            user=auth.authenticate(username=uname,password=pward)
            if(user is not None):
                auth.login(request,user)
                return HttpResponseRedirect('/profile/')
            else:
                messages.error(request,"Invalid Username or Password")
        return render(request,'index.html')

def signup(request):
    if(request.method=='POST'):
        obj=AccountUser()
        obj.firstname=request.POST.get('firstname')
        obj.surname = request.POST.get('surname')
        obj.username = request.POST.get('username')
        pward = request.POST.get('password')
        obj.dob = request.POST.get('dob')
        obj.gender = request.POST.get('gender')

        user=User.objects.create_user(username=obj.username,
                                      password=pward)
        obj.save()
        return HttpResponseRedirect('/')
    return render(request,'signup.html')

def profile(request):
    user=User.objects.get(username=request.user)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin/')
    user=AccountUser.objects.get(username=request.user)
    return render(request,'profile.html',{"User":user})

def profile2(request):
    user=User.objects.get(username=request.user)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin/')
    user=AccountUser.objects.get(username=request.user)
    return render(request,'profile2.html',{"User":user})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")



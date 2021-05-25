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
    post = Post.objects.all()
    if(request.method == "POST"):
        p = Post()
        p.user=user
        p.content = request.POST.get('msg')
        p.pic = request.FILES.get('img')
        if(not p.content=="" or not p.pic==None):
            p.save()
        return HttpResponseRedirect('/')
    return render(request,'profile.html',{"User":user,"Post":post})

def profile2(request):
    user=User.objects.get(username=request.user)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin/')
    user=AccountUser.objects.get(username=request.user)
    return render(request,'profile2.html',{"User":user})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


def editprofile(request):
    user=User.objects.get(username=request.user)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin/')
    user=AccountUser.objects.get(username=request.user)
    if(request.method=="POST"):
        user.firstname = request.POST.get('firstname')
        user.surname = request.POST.get('surname')
        user.email = request.POST.get('email')
        if(not request.POST.get('dob')==""):
            user.dob = request.POST.get('dob')
        user.gender = request.POST.get('gender')
        if(request.FILES.get('img')):
            user.img=request.FILES.get('img')
        user.work = request.POST.get('work')
        user.qualification = request.POST.get('qualification')
        user.currentTown = request.POST.get('ctown')
        user.HomeTown = request.POST.get('htown')
        user.relationship = request.POST.get('relationship')
        user.save()
        return HttpResponseRedirect('/profile2/')
    return render(request,'editprofile.html',{"User":user})
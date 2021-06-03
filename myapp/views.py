from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.contrib.messages import error
from django.conf import settings
from django.core.mail import send_mail
from random import randint
from .models import *

otp=0


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
    post=post[::-1]
    if(request.method == "POST"):
        p = Post()
        p.user=user
        p.content = request.POST.get('msg')
        p.pic = request.FILES.get('img')
        p.video = request.FILES.get('video')

        if(not p.content=="" or not p.pic==None or not p.video==None):
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

def send_mailUser(email,message):
    subject="welcome to Chatbook"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email,]
    send_mail(subject,message,email_from,recipient_list)

def forgetpassword(request):
    global otp
    if (request.method == "POST"):
        email = request.POST.get('email')
        otp = randint(1000, 9999)
        msg = str(otp) + "This is one time password /n Please enter otp to reset password"
        send_mailUser(email,msg)
        return HttpResponseRedirect('/otp/')
    else:
        return render(request,'forget.html')

def otpOption(request):
    if(request.method=="POST"):
        inputotp=request.POST.grt('otp')
        if(int(inputotp)==int(otp)):
            return HttpResponseRedirect('/resetpassword/')
        else:
            error(request,"Invalid OTP")
            return HttpResponseRedirect('/otp/')
    else:
        return render(request,'otp.html')

def resetPassword(request):
    if(request.method=="POST"):
        pward=request.POST.get('password')
        username=request.POST.get('uname')
        user=User.objects.get(username=username)
        user.set_password(pward)
        user.save()
        return HttpResponseRedirect('/')
    else:
        return render(request,'reset.html')




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

def likesystem(request,pid,uid):
    post=Post.objects.get(pid=pid)
    user=AccountUser.objects.get(uid=uid)
    try:
        like=Like.objects.get(post=post)
    except:
        like=Like
        like.save()
    lusers=like.user.all()
    if(user in lusers):
        like.counter-=1
        like.user.remove(user)
        like.save()
    else:
        like.counter+=1
        like.post=post
        like.user.add(user)
        like.save()
    return HttpResponseRedirect('/')




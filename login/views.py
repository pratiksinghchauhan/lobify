# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate,login 
from .forms import signupform
from .models import category
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.



def home(request):
    user = None
    if request.user.is_authenticated:
        return HttpResponseRedirect("/userhome/")
    if request.method == "POST" and 'custname' in request.POST and 'custpassword' in request.POST:
        username=request.POST.get("custname")
        password=request.POST.get("custpassword")
        print password

        user=User.objects.create_user(username = username,password = password)
        customer = category(user = user,customer=True)
        customer.save()
        return render(request,"home.html",{"message" : "User Created.. Please Login!!"})
            
    
    if request.method == "POST" and 'sellername' in request.POST  and 'sellerpassword' in request.POST:
        username=request.POST.get("sellername")
        password=request.POST.get("sellerpassword")

        print("here")

        user=User.objects.create_user(username = username,password = password)
        customer = category(user = user,customer=False)
        customer.save()
        return render(request,"home.html",{"message" : "User Created.. Please Login!!"})
    
    if request.method == "POST" and 'loginuser' in request.POST  and 'loginpass' in request.POST:
        username = request.POST['loginuser']
        password = request.POST['loginpass']
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request,user)
        return HttpResponseRedirect('/userhome/')

   
    return render(request,"home.html")


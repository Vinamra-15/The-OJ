from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def loginUser(request):
    if(request.method=="POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
            
            
        else:
            messages.error(request,"Invalid Credentials! Please use correct username and password!")
    return render(request,'login.html')


def logoutUser(request):
    if not request.user.is_anonymous:
        logout(request)
        messages.success(request,"Successfully Logged Out! Please Login to continue")
    return redirect("/login")

def registerUser(request):
    if(request.method=="POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        confirmPassword = request.POST["confirmPassword"]
        if password!=confirmPassword:
            messages.error(request,"Passwords do not match!")
            return redirect("/register")
        if len(password)<8:
            messages.error(request,"Password too small! Create a stronger password")
            return redirect("/register")

       
        if User.objects.filter(username=username).count()!=0:
            messages.error(request,"Username already taken!")
            return redirect("/register")
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        messages.success(request,"Account created successfully! Please Login")
        return redirect("/login")
    
    return render(request,'register.html')


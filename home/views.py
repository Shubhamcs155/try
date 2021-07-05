from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# from django.contrib.auth import 
# password for harry is harryharry

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        # print("hello")
        return redirect("/login")
    return render(request,"index.html")

def loginUser(request):
    if request.method == "POST":
        
        # check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        if user is not None:
            
            login(request,user)
            print("loggd in")
            return redirect("/")
        else:
            return render(request,"login.html")
    else:
        print("**************some problem*****************")
        return render(request,'login.html')

    

def logoutUser(request):
    logout(request)
    return redirect("/login")


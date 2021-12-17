from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        Password = request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        first_name = request.POST['first_name']
        last_name= request.POST['last_name']
        if cpassword==Password :
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, password=Password,
                                                username=username, email=email)
                user.save()
                print("user created")
                messages.info(request, "user created")
                return redirect("login")








        else:
            print("passsword donot match")
            messages.info(request,"password is not matching")
            return  redirect("register")


    return  render(request,"register.html")



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
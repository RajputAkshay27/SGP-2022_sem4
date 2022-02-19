from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.

def home(request):

    if request.method == 'POST':
        username = request.POST['UserName']
        password = request.POST['Password']

        user = authenticate(username = username,password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return HttpResponse("Super User")
            else:
                return HttpResponse("correct Credentials")
        else:
            return HttpResponse("Bad Credentials")
    
    return render(request,'Login/Loginpage.html')

def register(request):
    
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        Email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        user_type = request.POST['user_type']
        if User.objects.filter(username=username):
            messages.error(request,'Username already exist.')   
        elif User.objects.filter(email=Email):
            messages.error(request,'Email already exists')
        else:
            if user_type == 'super user':
                newuser = User.objects.create_superuser(username,Email,password)
            else:
                newuser = User.objects.create_user(username,Email,password)  
            newuser.first_name = fname
            newuser.last_name = lname
            
            newuser.save()
            messages.success(request,"New User has been added.")
    if request.method == 'GET':   
        if request.user.is_staff:                    
            return render(request,'Login/Registration.html')
        else:
            return HttpResponseForbidden("<h1> 403 Forbidden <br> Please login as super user to access this page.</h1>")

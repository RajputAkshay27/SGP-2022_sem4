from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render

# Create your views here.

def home(request):

    if request.method == 'POST':
        username = request.POST['UserName']
        password = request.POST['Password']

        user = authenticate(username = username,password=password)

        if user is not None:
            login(request, user)
            return redirect('/home')
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
                newuser = User.objects.create_user(username,Email,password)
                u_group = Group.objects.get(name = 'TTcommitte')
                u_group.user_set.add(newuser)
            else:
                newuser = User.objects.create_user(username,Email,password)  
                u_group = Group.objects.get(name = 'faculty')
                u_group.user_set.add(newuser)
            newuser.first_name = fname
            newuser.last_name = lname
            
            newuser.save()
            messages.success(request,"New User has been added.")
    if request.method == 'GET':   
        if is_TTcommitte(request.user):                    
            return render(request,'Login/Registration.html')
        else:
            return HttpResponseForbidden("<h1> 403 Forbidden <br> Please login as super user to access this page.</h1>")

def index(request):
    # if request.user.is_authenticated:
    #     if is_TTcommitte(request.user):
            return render(request,"homepage.html")
    #     else:
    #         return render(request,'n_userhome.html')
    # else:
    #         return HttpResponseForbidden("<h1> 403 Forbidden <br> Please login first.</h1>")

def logout_user(request):
        logout(request)
        return redirect('/login')
    
def is_TTcommitte(user):
    return user.groups.filter(name = 'TTcommitte').exists()
    
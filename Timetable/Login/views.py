from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):

    if request.method == 'POST':
        username = request.POST['UserName']
        password = request.POST['Password']

        user = authenticate(username = username,password=password)

        if user is not None:
            login(request , user)
            return HttpResponse("correct Credentials")
        else:
            return HttpResponse("Bad Credentials")

    return render(request,'Login/Loginpage.html')

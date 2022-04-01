from django.shortcuts import render

# Create your views here.

def fac_alloc(request):
    return render(request,'faculty_allocation/facalloction.html')
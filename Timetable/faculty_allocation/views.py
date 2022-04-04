from django.shortcuts import render
from selection.models import subject,faculty

# Create your views here.

def fac_alloc(request):
    subs = subject.objects.all()
    fac = faculty.objects.all()
    Allocated_fac = request.POST.get('Faculty',False)
    
    return render(request,'faculty_allocation/facalloction.html',{"sub":subs ,"fac":fac})
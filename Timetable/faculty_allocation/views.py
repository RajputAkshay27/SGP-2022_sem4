from django.shortcuts import render
from selection.models import faculty, subject

from .models import faculty_alloc

# Create your views here.

def fac_alloc(request):
    subs = subject.objects.all()
    fac_op = faculty.objects.all()
    if request.method == 'POST':
        sem = request.POST['Semester']
        sub = request.POST['Subject']
        lect_type = request.POST['lec_type']
        s = subject.objects.get(sub_name = sub)
        Allocated_fac = request.POST.getlist("Faculty")
        for fac in Allocated_fac:
            f = faculty.objects.get(fac_code = fac)
            data = faculty_alloc(Semester = sem,Subject_Code = s , lecture_Type = lect_type, Faculty_Name = f)
            try:
                data.save() 
            except:
                print("data already exists")
        return render(request,'faculty_allocation/facalloction.html',{"sub":subs ,"fac":fac_op})
    else:
        return render(request,'faculty_allocation/facalloction.html',{"sub":subs ,"fac":fac_op})

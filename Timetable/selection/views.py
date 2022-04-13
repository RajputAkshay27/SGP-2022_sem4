from django.shortcuts import render
from .models import faculty, subject, priority

# Create your views here.

def selection(request):
    name = request.user.first_name
    if request.method == "POST":
        semester = request.POST['Semester']
        SP1 = request.POST['subjectPriority1']
        SP2 = request.POST['subjectPriority2']
        SP3 = request.POST['subjectPriority3']
        PP1 = request.POST['Practical1']
        PP2 = request.POST['Practical2']
        PP3 = request.POST['Practical3']
        
        S1 = subject.objects.get(sub_name = SP1)
        S2 = subject.objects.get(sub_name = SP2)
        S3 = subject.objects.get(sub_name = SP3)
        P1 = subject.objects.get(sub_name = PP1)
        P2 = subject.objects.get(sub_name = PP2)
        P3 = subject.objects.get(sub_name = PP3)
        
        facultyCode = faculty.objects.get(fac_name = name)
        
        data = priority()
        data.semester = semester
        data.fac_code = facultyCode
        data.Theory_Priority1 = S1
        data.Theory_Priority2 = S2
        data.Theory_Priority3 = S3
        data.Practical_Priority1 = P1
        data.Practical_Priority2 = P2
        data.Practical_Priority3 = P3
        
        try: 
            data.save()
        except:
            print('some error occured')
        
    else:
        subs = subject.objects.all()
        sem = range(1,8)
        return render (request, 'selection/selection.html',{"name":name,"subs":subs,"sem":sem})

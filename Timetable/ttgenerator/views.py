from django.shortcuts import render
from selection.models import resource,subject

# Create your views here.

def index(request):
    sem = range(1,8)
    timeslots = ['9:10 - 10:10','10:10 - 11:10','12:10 - 01:10','01:10 - 02:10','02:20 - 03:20','03:20 - 04:20']
    day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    room = resource.objects.all()
    subs =  subject.objects.all()
    return render(request,'ttgenerator/timeTable.html',{'tslot':timeslots,'day':day,'sem':sem,'room':room,"subs":subs})
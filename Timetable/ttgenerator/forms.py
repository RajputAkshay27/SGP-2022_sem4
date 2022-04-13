from django import forms
from selection.models import faculty, subject, resource

class ttform(forms.Form):
    timeslotoptions = [
        '09:10 - 10:10','10:10 - 11:10','12:10 - 01:10','01:10 - 02:10','02:20 - 03:20','03:20 - 04:20',]
    
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    
    semester = ['1','2','3','4','5','6','7','8']
    
    sem = forms.ChoiceWidget(choices= semester)
    day = forms.ChoiceWidget(choices= days)
    timeslot = forms.ChoiceWidget(choices= timeslotoptions)
    
    
    
    
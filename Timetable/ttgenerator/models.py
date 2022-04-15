from django import forms
from django.db import models
from selection.models import faculty, subject, resource
# Create your models here.

class timeTable(models.Model):
    semester = models.CharField()
    timeslot = models.CharField()
    day = models.CharField()
    type = models.CharField()
    Tt_faculty = models.ForeignKey(faculty,on_delete=models.CASCADE)
    Room = models.ForeignKey(resource,on_delete=models.CASCADE)
    sub = models.ForeignKey(subject,on_delete=models.CASCADE)
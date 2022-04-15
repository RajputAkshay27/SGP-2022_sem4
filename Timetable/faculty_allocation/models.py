from django.db import models

from selection.models import faculty, subject

# Create your models here.

class faculty_alloc(models.Model):
    Semester = models.IntegerField()
    Subject_Code = models.ForeignKey(subject,on_delete=models.CASCADE)
    lecture_Type = models.CharField(max_length=10)
    Faculty_Name = models.ForeignKey(faculty,on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (('Semester','Subject_Code','Faculty_Name'))
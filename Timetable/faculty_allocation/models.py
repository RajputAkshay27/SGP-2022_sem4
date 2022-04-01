from enum import unique
from django.db import models
from selection.models import subject,faculty,resource
# Create your models here.

class faculty_alloc(models.Model):
    semester = models.IntegerField(max_length=2)
    subcode = models.ForeignKey(subject.sub_code,on_delete=models.CASCADE)
    lec_type = models.ForeignKey(resource.room_no,on_delete=models.CASCADE)
    faculty_n = models.ForeignKey(faculty.fac_code,on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.subcode
    
    class Meta:
        unique_together = (('semester','subcode','faculty_n'))
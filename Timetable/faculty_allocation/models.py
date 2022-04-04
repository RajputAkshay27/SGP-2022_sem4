from django.db import models
from selection.models import subject,faculty
# Create your models here.

class faculty_alloc(models.Model):
    semester = models.IntegerField()
    subcode = models.ForeignKey(subject,to_field='sub_code',on_delete=models.CASCADE)
    lec_type = models.CharField(max_length=10)
    faculty_n = models.ForeignKey(faculty,to_field='fac_code',on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.subcode
    
    class Meta:
        unique_together = (('semester','subcode','faculty_n'))
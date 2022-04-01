from django.db import models

# Create your models here.

class faculty_alloc(models.Model):
    semester = models.IntegerField(max_length=2)
    subcode = models.
    lec_type = models.CharField(max_length=10)
    faculty = models.ForeignKey(on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.subcode
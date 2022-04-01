from django.db import models

# Create your models here.

# class faculty(models.Model):
#     Name = models.CharField(max_length=25,primary_key=True)
#     f_code = models.CharField(max_length=10)

class faculty_alloc(models.Model):
    semester = models.IntegerField(default=4)
    subcode = models.CharField(max_length=10)
    lec_type = models.CharField(max_length=10)
    # faculty = models.ForeignKey(faculty.f_code,on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.subcode
from pickle import TRUE
from re import T
from django.db import models

# Create your models here.

class faculty(models.Model):
    fac_code = models.CharField(max_length=7,primary_key=TRUE)
    fac_name = models.CharField(max_length=25)

    def __str__(self):
        return self.fac_code

class subject(models.Model):
    sub_code = models.CharField(max_length=10,primary_key=True)
    sub_name = models.CharField(max_length=30)

    def __str__(self):
        return self.sub_code


class resource(models.Model):
    room_no = models.CharField(max_length=5,primary_key=True)
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.room_no


# class priority(models.Model):
#     semester = models.IntegerField(max_length=2)
#     fac_code = models.CharField(max_length=7)
    

    

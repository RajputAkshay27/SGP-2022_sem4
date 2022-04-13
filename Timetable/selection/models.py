from django.db import models

# Create your models here.

class faculty(models.Model):
    fac_code = models.CharField(max_length=7,primary_key=True)
    fac_name = models.CharField(max_length=25)

    def __str__(self):
        return self.fac_code

class subject(models.Model):
    sub_code = models.CharField(max_length=10,primary_key=True)
    sub_name = models.CharField(max_length=30)

    def __str__(self):
        return self.sub_name


class resource(models.Model):
    room_no = models.CharField(max_length=5,primary_key=True)
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.room_no
    

class priority(models.Model):
    semester = models.IntegerField()
    fac_code = models.ForeignKey(faculty,to_field='fac_code',on_delete=models.CASCADE)
    Theory_Priority1 = models.CharField(max_length=10)
    Practical_Priority1 = models.CharField(max_length=10)
    Theory_Priority2 = models.CharField(max_length=10)
    Practical_Priority2 = models.CharField(max_length=10)
    Theory_Priority3 = models.CharField(max_length=10)
    Practical_Priority3 = models.CharField(max_length=10)
    
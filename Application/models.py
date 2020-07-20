from django.db import models
import datetime

class StudentRegister(models.Model):
    regno  = models.AutoField(primary_key = True)
    Name = models.CharField(max_length=50)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(max_length=50,unique=True)
    user = models.CharField(max_length=50,unique=True)
    pas = models.CharField(max_length=50)

class ScheduleNewClass(models.Model):
    regn = models.AutoField(primary_key=True)
    cname = models.CharField(unique=True,max_length=50)
    Faculty = models.CharField(max_length=50)
    Date = models.DateField(default=datetime.date(2020,1,1))
    Time = models.TimeField(default=datetime.time(2,30,5))
    Fee =  models.FloatField(max_length=90000)
    Duration = models.IntegerField()


class EnroleCoueses(models.Model):
    Register_No = models.AutoField(primary_key = True)
    Course_Name = models.CharField(max_length=50)
    Faculty_Name = models.CharField(max_length=50)
    date = models.DateField(default=datetime.date(2020,1,1))
    timing = models.TimeField(default=datetime.time(00,00))
    Student_Name = models.CharField(max_length=50)
    Student_Contact = models.IntegerField(unique=True)
    Enroll_status = models.CharField(max_length=10)

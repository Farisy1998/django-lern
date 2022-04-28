from django.db import models

class Teachers(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phno=models.IntegerField(max_length=12)
    uname=models.CharField(max_length=20)
    pswd=models.CharField(max_length=20)
    cpswd=models.CharField(max_length=20)

class Assignment(models.Model):
    sem=models.CharField(max_length=15)
    course=models.CharField(max_length=50)
    topic=models.CharField(max_length=100)
    sub_date=models.CharField(max_length=25)

class StudyMaterials(models.Model):
    sem=models.CharField(max_length=15)
    course=models.CharField(max_length=50)
    material=models.FileField()

class Classes(models.Model):
    sem=models.CharField(max_length=15)
    course=models.CharField(max_length=50)
    class_link=models.CharField(max_length=700)
    date=models.DateField(max_length=20)
    start_time=models.TimeField(max_length=20)
    end_time=models.TimeField(max_length=20)

class Exams(models.Model):
    sem=models.CharField(max_length=15)
    course=models.CharField(max_length=50)
    date=models.DateField(max_length=20)
    start_time=models.TimeField(max_length=20)
    end_time=models.TimeField(max_length=20)
    qp=models.FileField()

class Photos(models.Model):
    title=models.CharField(max_length=105)
    photo=models.FileField()
    descr=models.CharField(max_length=700)

def __str__(self):
        return self.uname
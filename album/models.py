from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length = 30,unique=True)
    count_teachers = models.IntegerField(blank=True ,null=True)

    class Meta:
        ordering = ['count_teachers', 'name']
        
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.SET_NULL)
    subjects_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['subjects_count', 'surname', 'name']


class Class(models.Model):
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    mail = models.EmailField(max_length=50, unique=True)
    clas = models.ForeignKey(Class, null=False, blank=False, on_delete=models.DO_NOTHING)
    birthday = models.DateField()

    class Meta:
        ordering = ['birthday', 'clas', 'surname', 'name']

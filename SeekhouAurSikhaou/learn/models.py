from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime 


# Create your models here.

class User(AbstractUser):
    TYPE_OPTIONS = [
        ('STUDENT', 'student'),
        ('TEACHER', 'teacher'),
        ('PARENT', 'parent'),
    ]
    type = models.CharField(max_length=7, choices=TYPE_OPTIONS, default='STUDENT', blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="users")

class Course(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    start_date = models.DateField(auto_now = datetime.datetime.now())
    end_date = models.DateField()
    # Duration 
    Status = models.BooleanField(default = True)
    
class Section(models.Model):
    TERM_OPTIONS = [
        ('FALL','Fall'),
        ('WINTER','Winter'),
        ('SUMMER','Summer')
    ]
    name = models.CharField(max_length = 150)
    description = models.TextField()
    start_date = models.DateField(auto_now = datetime.datetime.now())
    end_date = models.DateField()
    # Duration = 
    status = models.BooleanField(default = True)
    academic_year = models.PositiveSmallIntegerField()
    academic_term = models.CharField(max_length=1000, choices=TERM_OPTIONS, default='FALL', blank=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="sections")
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="sections")



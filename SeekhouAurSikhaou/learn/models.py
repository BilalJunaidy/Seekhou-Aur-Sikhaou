from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime 
from django.utils import timezone


# Create your models here.

class User(AbstractUser):
    TYPE_OPTIONS = [
        ('STUDENT', 'student'),
        ('TEACHER', 'teacher'),
        ('PARENT', 'parent'),
    ]
    GRADE_OPTIONS = [
        ('GRADE5','Grade 5')
        ('GRADE6','Grade 6')
        ('GRADE7','Grade 7')
        ('GRADE8','Grade 8')
        ('GRADE9','Grade 9')
        ('GRADE10','Grade 10')
        ('GRADE11','Grade 11')
        ('GRADE12','Grade 12')
        ('GRADE13','Grade 13')    
    ]
    type = models.CharField(max_length=7, choices=TYPE_OPTIONS, default='STUDENT', blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="users")
    profile_image = models.ImageField()
    grade_level = models.CharField(max_length=6, choices=GRADE_OPTIONS, blanl=False)
    


class Course(models.Model):
    name = models.CharField(max_length = 150)
    code = models.CharField(max_length = 100)
    description = models.TextField()
    start_date = models.DateField()

    # For now I have changed the default value of the datefield to be equal to datetime.datetime.now since I would like the user to define this field 
    # To come back to this in the continous improvement phase (post-Hackathon)
    # start_date = models.DateField(auto_now = datetime.datetime.now())
    
    end_date = models.DateField()
    # Duration 
    Status = models.BooleanField(default = True)
    date_created = models.DateTimeField(default = timezone.now)
    
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
    date_created = models.DateTimeField(default = timezone.now)


class Lecture(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="lectures")
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name="lectures")
    number = models.IntegerField()
    name = models.CharField(max_length = 255, default = "any")
    description = models.TextField()
    lecture_date = models.DateField()
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    date_created = models.DateTimeField(default = timezone.now)
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="lectures")

# class Lecture_Note(models.Model):
#     section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name="lectures")
#     teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="sections")
#     title
#     notes
#     date_created
#     files




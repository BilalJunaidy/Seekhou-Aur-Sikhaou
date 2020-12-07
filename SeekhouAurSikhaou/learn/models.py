from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime 
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    TYPE_OPTIONS = [
        ('STUDENT', 'Student'),
        ('TEACHER', 'Teacher'),
        ('PARENT', 'Parent'),
        ('ADMIN', 'Admin')
    ]
    GRADE_OPTIONS = [
        ('GRADE5','Grade 5'),
        ('GRADE6','Grade 6'),
        ('GRADE7','Grade 7'),
        ('GRADE8','Grade 8'),
        ('GRADE9','Grade 9'),
        ('GRADE10','Grade 10'),
        ('GRADE11','Grade 11'),
        ('GRADE12','Grade 12'),
        ('GRADE13','Grade 13'),   
    ]

    GENDER_OPTIONS = [
        ('MALE','Male'),
        ('FEMALE','Female'),
    ]
    # profile_image = models.ImageField(null=False, blank=False)
    grade_level = models.CharField(max_length=7, choices=GRADE_OPTIONS, blank=False, default='GRADE5')
    type = models.CharField(max_length=7, choices=TYPE_OPTIONS, default='STUDENT', blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="users")
    gender = models.CharField(max_length=6, choices=GENDER_OPTIONS, blank=False, default='MALE')

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
    academic_term = models.CharField(max_length=6, choices=TERM_OPTIONS, default='FALL', blank=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="sections")
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="sections")
    date_created = models.DateTimeField(default = timezone.now)


class Lecture(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="lectures")
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name="lectures")
    number = models.IntegerField()
    name = models.CharField(max_length = 255)
    description = models.TextField()
    lecture_date = models.DateField()
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    date_created = models.DateTimeField(default = timezone.now)
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="lectures")

class Attendance(models.Model):
    ATTENDANCE_OPTIONS = [
        ('PRESENT','Present'),
        ('ABSENT','Absent')
    ]
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name="attendances")

    # Although initially it does appears as though including a course field is overkill. 
    # However, I think it will be beneficials for management/teachers to review the attendances over the entire course object vs just over a section.
    # This might give them an insight into which course(s) students are finding more interesting and which ones they are not, and hence, using 
    # this information, management/teachers will be able to adjust course and section offerings accordingly. 
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="attendances")
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name="attendances")
    status = models.CharField(max_length=7, choices = ATTENDANCE_OPTIONS, default = 'PRESENT')
    student = models.ManyToManyField('User', blank=False, related_name = "attendances")
    teacher_comments = models.TextField()

class Lecture_Note(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name="lecturenotes")
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="lecturenotes")
    title = models.CharField(max_length = 255)
    notes = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    files = models.FileField()

class Comment(models.Model):
    lecture_note = models.ForeignKey('Lecture_Note', on_delete=models.CASCADE, related_name="comments")
    student = models.ForeignKey('User', on_delete=models.CASCADE, related_name="comments")
    title = models.CharField(max_length = 255)
    comment = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)

class Assignment(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="assignments")
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name="assignments")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default = timezone.now)
    files = models.FileField()
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="assignments")

class Submission(models.Model):
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey('User', on_delete=models.CASCADE, related_name="submissions")
    title = models.CharField(max_length = 255)
    description = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    files = models.FileField()

class Mark(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="marks")
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name="marks")
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE, related_name="marks")
    student = models.ForeignKey('User', on_delete=models.CASCADE, related_name="marks")
    # teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="marks")
    date_created = models.DateTimeField(default = timezone.now)
    marks = models.FloatField() 
    teacher_comments = models.TextField()














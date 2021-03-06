from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime 
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
import datetime 

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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
    grade_level = models.CharField(max_length=7, choices=GRADE_OPTIONS, blank=True, default='GRADE5')
    type = models.CharField(max_length=7, choices=TYPE_OPTIONS, default='STUDENT', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="users")
    gender = models.CharField(max_length=6, choices=GENDER_OPTIONS, null=True, blank=True, default='MALE')
    age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(7), MaxValueValidator(100)])
    is_teacher = models.BooleanField(_('Check box if the user is a teacher'), default = False)
    is_student = models.BooleanField(_('Check box if the user is a student'), default = False)

    def __str__(self):
        return f"{self.type} - {self.first_name} {self.last_name}"





# The following were my unsuccesful attemtps at validating the start and end date fields. 

# user_entered_course_start_date = datetime.date.today()
# first_attempt = True

# def validatedates(value, first_attempt, user_entered_course_start_date):
#     if first_attempt == False:
#         if value < user_entered_course_start_date:
#             raise ValidationError(
#             _('The end date of the course can not be before the start date'),
#             params={'value': value},
#         )            
#     else:
#         user_entered_course_start_date = value
#         first_attempt = False
#         return value 

    # print(user_entered_course_start_date)
    # user_entered_course_start_date = value
    # print(user_entered_course_start_date)
    # if user_entered_course_start_date < value: 
    # # if value != 'bhainscourse':
    # #     print(type(value))
    # #     print(value)
    #     raise ValidationError(
    #         _('%(value)s is not a legit course name'),
    #         params={'value': value},
    #     )


class Course(models.Model):
    name = models.CharField(max_length = 150)
    code = models.CharField(max_length = 100)
    description = models.TextField()
    # start_date = models.DateField(validators=[validatedates])
    start_date = models.DateField()

    # For now I have changed the default value of the datefield to be equal to datetime.datetime.now since I would like the user to define this field 
    # To come back to this in the continous improvement phase (post-Hackathon)
    # start_date = models.DateField(auto_now = datetime.datetime.now())
    
    # end_date = models.DateField(validators=[validatedates])
    end_date = models.DateField()

    Status = models.BooleanField(_('Course active or not'), default = True)
    date_created = models.DateTimeField(default = timezone.now)

# The following were my unsuccesful attemtps at validating the start and end date fields. 
# This whole clean shit needed to be in the modelform class not the model class itself. 

    # def clean(self):
    #     cleaned_data = super(request.POST)
    #     # cleaned_data = super().clean()
    #     start_date_entered = cleaned_data.get("start_date")
    #     end_date_entered = cleaned_data.get("end_date")

    #     if start_date_entered and end_date_entered:
    #         if start_date_entered > end_date_entered:
    #             raise ValidationError(_('The end date of the course can not be before the start date'))

    def __str__(self):
        return f"{self.name} - {self.code}"
        

    
class Section(models.Model):
    TERM_OPTIONS = [
        ('FALL','Fall'),
        ('WINTER','Winter'),
        ('SUMMER','Summer')
    ]
    name = models.CharField(max_length = 150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    # Duration = 
    status = models.BooleanField(_('Section active or not'), default = True)
    academic_year = models.PositiveSmallIntegerField(default = datetime.date.today().year, validators = [MinValueValidator(datetime.date.today().year - 5), MaxValueValidator(datetime.date.today().year + 5)])
    academic_term = models.CharField(max_length=6, choices=TERM_OPTIONS, default='FALL', blank=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="sections")
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="sections")
    date_created = models.DateTimeField(default = timezone.now)
    student = models.ManyToManyField('User', blank=False, related_name = "section_students")

    def __str__(self):
        return f"{self.name} - {self.teacher} - {self.academic_term} - {self.academic_year}"


class Lecture(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="lectures")
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name="lectures")
    # I don't think we would need the user to be inputting a number field for lectures especially considering (atleast for now)
    # I am not giving users the ability to delete lectures. Therefore, the id field of the Lecture object should be fine since it will autoincrement
    # number = models.IntegerField()
    name = models.CharField(max_length = 255)
    description = models.TextField()
    lecture_date = models.DateField()                       
    start_time = models.TimeField()
    end_time = models.TimeField()
    date_created = models.DateTimeField(default = timezone.now)
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="lectures")

    def __str__(self):
        return f"{self.id} - {self.teacher.username} - {self.name} - {self.lecture_date}"


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
    attendance_status = models.CharField(max_length=7, choices = ATTENDANCE_OPTIONS, default = 'PRESENT')
    student = models.ManyToManyField('User', blank=False, related_name = "attendances")
    teacher_comments = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"{self.student.username} marked {self.attendance_status} for {self.lecture}"

class Lecture_Note(models.Model):
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name="lecturenotes")
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name="lecturenotes")
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="lecturenotes")
    title = models.CharField(max_length = 255)
    notes = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    # files = models.FileField()

    def __str__(self):
        return f"{self.id} - {self.title} - {self.date_created}"

class Comment(models.Model):
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name="comments")
    lecture_note = models.ForeignKey('Lecture_Note', on_delete=models.CASCADE, related_name="comments")
    student = models.ForeignKey('User', on_delete=models.CASCADE, related_name="comments")
    title = models.CharField(max_length = 255)
    comment = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"{self.student.username} commented on lecture {self.lecture.id} on {self.date_created}"

class Assignment(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="assignments")
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name="assignments")
    deadline = models.DateTimeField()
    # end_date = models.DateField()
    # end_time = models.TimeField()
    status = models.BooleanField(_('Assignment available or not'),default=True)
    date_created = models.DateTimeField(default = timezone.now)
    # files = models.FileField()
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="assignments")

    def __str__(self):
        return f"Assignment # {self.id} {self.title} due on {self.deadline}"

class Submission(models.Model):
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey('User', on_delete=models.CASCADE, related_name="submissions")
    teacher = models.ForeignKey('User', on_delete=models.CASCADE, null=True, related_name="submissions_teacher")
    title = models.CharField(max_length = 255)
    description = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"{self.student} submission to {self.teacher} for {self.assignment}"
    
    # files = models.FileField()

class Mark(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="marks")
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name="marks")
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE, related_name="marks")
    student = models.ForeignKey('User', on_delete=models.CASCADE, related_name="marks")
    # teacher = models.ForeignKey('User', on_delete=models.CASCADE, related_name="marks")
    date_created = models.DateTimeField(default = timezone.now)
    marks = models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(100)]) 
    teacher_comments = models.TextField(null=True, blank=True) 














from django.contrib import admin
from .models import User, Course, Section, Lecture, Attendance, Lecture_Note, Comment, Assignment, Submission, Mark


# Register your models here.

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lecture)
admin.site.register(Attendance)
admin.site.register(Lecture_Note)
admin.site.register(Comment)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Mark)
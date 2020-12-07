from django.contrib import admin
from .models import User, Course, Section, Lecture, Attendance, Lecture_Note, Comment


# Register your models here.

admin.site.register(User)

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lecture)
admin.site.register(Attendance)
admin.site.register(Lecture_Note)
admin.site.register(Comment)
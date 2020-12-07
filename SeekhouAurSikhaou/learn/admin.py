from django.contrib import admin
# from .models import Course, Section, Lecture, Attendance, Lecture_Note, Comment
# from .models import User

from .models import User, StudentProfile, TeacherProfile, ParentProfile

# Register your models here.

# admin.site.register(User)
admin.site.register(StudentProfile)
admin.site.register(ParentProfile)
admin.site.register(TeacherProfile)

# admin.site.register(Course)
# admin.site.register(Section)
# admin.site.register(Lecture)
# admin.site.register(Attendance)
# admin.site.register(Lecture_Note)
# admin.site.register(Comment)
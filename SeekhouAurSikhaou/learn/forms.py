from django.forms import ModelForm

from .models import User, Course, Section, Lecture, Attendance, Lecture_Note, Comment, Assignment, Submission, Mark


class userform(ModelForm):
    class Meta:
        model = User
        # fields = ['username','password','first_name','last_name','email','type','parent', 'grade_level', 'profile_image']
        fields = ['username','password','first_name','last_name','email','type','parent', 'grade_level', 'gender']
        
class courseform(ModelForm):
    class Meta:
        model = Course 
        fields = '__all__'
    
class sectionform(ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

class lectureform(ModelForm):
    class Meta:
        model = Lecture 
        fields = '__all__'

class attendanceform(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

class lecturenoteform(ModelForm):
    class Meta:
        model = Lecture_Note
        fields = '__all__'

class commentform(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class assignmentform(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'

class submissionform(ModelForm):
    class Meta:
        model = Submission
        fields = '__all__'

class markform(ModelForm):
    class Meta:
        model = Mark
        fields = '__all__'
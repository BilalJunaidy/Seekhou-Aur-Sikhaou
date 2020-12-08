from django.forms import ModelForm
from django import forms 
from .models import User, Course, Section, Lecture, Attendance, Lecture_Note, Comment, Assignment, Submission, Mark
from django.core.exceptions import ValidationError
import datetime 


class DatePicker(forms.DateInput):
    # input_type = 'datetime-local'
    input_type = 'date'

class TimePicker(forms.TimeInput):
    input_type = 'time'


class userform(ModelForm):
    class Meta:
        model = User
        # fields = ['username','password','first_name','last_name','email','type','parent', 'grade_level', 'profile_image']
        fields = ['username','password','first_name','last_name','email','type','parent', 'grade_level', 'gender', 'age']
        
class courseform(ModelForm):
    class Meta:
        model = Course 
        exclude = ['date_created']
        widgets = {"start_date": DatePicker(),
                   "end_date": DatePicker(),
        }

# Need to look into validating modelforms during the 2nd iteration of this application.
# The following would be good places to start in terms of researching:
# 1. https://stackoverflow.com/questions/13845795/django-custom-validation-of-multiple-fields
# 2. https://django.cowhite.com/blog/django-form-validation-and-customization-adding-your-own-validation-rules/
# 3. http://www.learningaboutelectronics.com/Articles/How-to-create-a-custom-field-validator-in-Django.php
# 4. https://stackoverflow.com/questions/12806771/django-modelform-validation
# 5. https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#overriding-the-clean-method
# I also need to understand this super and the clean thing and how the whole flow of this modelform validation works in the back end

    def __init__(self, *args, **kwargs):
        super(courseform, self).__init__(*args, **kwargs)
    
    def clean(self):
        """
        In here you can validate the two fields
        raise ValidationError if you see anything goes wrong. 
        for example if you want to make sure that field1 != field2
        """
        super(courseform, self).clean()
        start = self.cleaned_data['start_date']
        end = self.cleaned_data['end_date']

        if start > end:
            self.add_error('start_date', 'The Start date of the course can not be after the End date')
            self.add_error('end_date', 'The End date of the course can not be before the Start date')

    
class sectionform(ModelForm):
    class Meta:
        model = Section
        exclude = ['date_created']
        widgets = {"start_date": DatePicker(),
                   "end_date": DatePicker(),
        }

    def __init__(self, *args, **kwargs):
        super(sectionform, self).__init__(*args, **kwargs)
    
    def clean(self):
        """
        In here you can validate the two fields
        raise ValidationError if you see anything goes wrong. 
        for example if you want to make sure that field1 != field2
        """
        super(sectionform, self).clean()
        start = self.cleaned_data['start_date']
        end = self.cleaned_data['end_date']

        if start > end:
            self.add_error('start_date', 'The Start time of the course can not be after the End time')
            self.add_error('end_date', 'The End time of the course can not be before the Start time')
        
        teacher = self.cleaned_data['teacher']
        if teacher.type != 'TEACHER':
            self.add_error('teacher', f'You need to select a teacher for this lecture. Currently you selected {teacher.username}, who is a {teacher.type.lower()}')

class lectureform(ModelForm):
    class Meta:
        model = Lecture 
        exclude = ['date_created']
        widgets = {"lecture_date": DatePicker(),
                   "start_time": TimePicker(),
                   "end_time": TimePicker(),
                    }
    def __init__(self, *args, **kwargs):
        super(lectureform, self).__init__(*args, **kwargs)
    
    def clean(self):
        """
        In here you can validate the two fields
        raise ValidationError if you see anything goes wrong. 
        for example if you want to make sure that field1 != field2
        """
        super(lectureform, self).clean()
        start = self.cleaned_data['start_time']
        end = self.cleaned_data['end_time']

        if start > end:
            self.add_error('start_time', 'The Start date of the course can not be after the End date')
            self.add_error('end_time', 'The End date of the course can not be before the Start date')

        teacher = self.cleaned_data['teacher']
        if teacher.type != 'TEACHER':
            self.add_error('teacher', f'You need to select a teacher for this lecture. Currently you selected {teacher.username}, who is a {teacher.type.lower()}')
        
        lecture_date = self.cleaned_data['lecture_date']
        if lecture_date < datetime.date.today():
            self.add_error('lecture_date', f'Todays date is {datetime.date.today()}, and you are trying to create a lecture for {lecture_date}. You can not create a lecture the lecture date of which has already passed')

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
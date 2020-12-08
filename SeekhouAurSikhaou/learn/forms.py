from django.forms import ModelForm
from django import forms 
from .models import User, Course, Section, Lecture, Attendance, Lecture_Note, Comment, Assignment, Submission, Mark
from django.core.exceptions import ValidationError


class DatePicker(forms.DateInput):
    # input_type = 'datetime-local'
    input_type = 'date'


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
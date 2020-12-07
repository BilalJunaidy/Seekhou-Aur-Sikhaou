from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.forms import ModelForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError

from .models import User 

# from .models import User, Course, Section, Lecture, Attendance, Lecture_Note, Comment, Assignment, Submission, Mark

# Create your views here.

# @login_required(login_url='login')
def index(request):
    a = User.objects.get(pk = request.user.id)
    b = a.studentprofile.type
    return HttpResponse(f"{request.user}, {b}")
    # return HttpResponse(f"{request.user.type}, {request.user.first_name}, {type(request.user)},{request.user.id}")
    # class userform(ModelForm):
    #     class Meta:
    #         model = User
    #         fields = ['username','password','first_name','last_name','email','type','parent', 'grade_level', 'profile_image', 'is_staff']
    
    # class courseform(ModelForm):
    #     class Meta:
    #         model = Course 
    #         fields = '__all__'
        
    # class sectionform(ModelForm):
    #     class Meta:
    #         model = Section
    #         fields = '__all__'

    # class lectureform(ModelForm):
    #     class Meta:
    #         model = Lecture 
    #         fields = '__all__'
    
    # class attendanceform(ModelForm):
    #     class Meta:
    #         model = Attendance
    #         fields = '__all__'
    
    # class lecturenoteform(ModelForm):
    #     class Meta:
    #         model = Lecture_Note
    #         fields = '__all__'
    
    # class commentform(ModelForm):
    #     class Meta:
    #         model = Comment
    #         fields = '__all__'
    
    # class assignmentform(ModelForm):
    #     class Meta:
    #         model = Assignment
    #         fields = '__all__'
    
    # class submissionform(ModelForm):
    #     class Meta:
    #         model = Submission
    #         fields = '__all__'

    # class markform(ModelForm):
    #     class Meta:
    #         model = Mark
    #         fields = '__all__'
    
    
    # userform = userform()
    # courseform = courseform()
    # sectionform = sectionform()
    # lectureform = lectureform()
    # attendanceform = attendanceform()
    # lecturenoteform = lecturenoteform()
    # commentform = commentform()
    # assignmentform = assignmentform()
    # submissionform = submissionform()
    # markform = markform() 



    return render(request, "learn/index.html", {
        # "userform":userform,
        "courseform":courseform,
        "sectionform":sectionform,
        "lectureform": lectureform,
        "attendanceform":attendanceform,
        "lecturenoteform":lecturenoteform,
        "commentform":commentform,
        "assignmentform":assignmentform,
        "submissionform":submissionform,
        "markform":markform,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        # username = 'bhainskitaang@gmail.com'
        # password = '12345678910'
        user = authenticate(request, username=email, password=password)
        # user = authenticate(request, username=bhainskitaang@gmail.com, password=12345678910)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "learn/login.html", {
                "message": "Invalid email and/or password.",
                "username":email,
                "password":password,
            })
    else:
        return render(request, "learn/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "learn/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "learn/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "learn/register.html")
        

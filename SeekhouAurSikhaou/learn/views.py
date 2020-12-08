from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError


from .forms import userform, courseform, sectionform, lectureform, attendanceform, lecturenoteform, commentform, assignmentform, submissionform, markform
from .helpers import validateusers
# , validatedates

# Create your views here.

# @login_required(login_url='login')
def index(request):

    user_form = userform(request.POST or None)
    course_form = courseform(request.POST or None)
    section_form = sectionform(request.POST or None)
    lecture_form = lectureform(request.POST or None)
    attendance_form = attendanceform(request.POST or None)
    lecturenote_form = lecturenoteform(request.POST or None)
    comment_form = commentform(request.POST or None)
    assignment_form = assignmentform(request.POST or None)
    submission_form = submissionform(request.POST or None)
    mark_form = markform(request.POST or None)

    if request.method == 'POST':
        
        # This two step validation process for the submitted form is very hacky in my opinion and I don't like it.
        # This needs to change in the next iteration of this web app.
        # Look into declaring a validator function and using that as the validator argument into the "parent" field in the User model class
        # This validator then needs to be connected to the ModelForm.

        # The following will take place when the form IS valid
        if user_form.is_valid():
            user_form.save(commit = False)
            return validateusers(request, user_form)

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/index.html", {
                "userform": user_form
            })
        
    # The following gets rendered when the client sends a GET request to the 'home/' route
    return render(request, "learn/index.html", {
        "userform":user_form,
        "courseform":course_form,
        "sectionform":section_form,
        "lectureform": lecture_form,
        "attendanceform":attendance_form,
        "lecturenoteform":lecturenote_form,
        "commentform":comment_form,
        "assignmentform":assignment_form,
        "submissionform":submission_form,
        "markform":mark_form,
    })


def course(request):
    if request.method == 'POST':
        course_form = courseform(request.POST)

        # The following will take place when the form IS valid
        if course_form.is_valid():
            course_form.save()
            # return validatedates(request, course_form)
            return HttpResponse("you have made a successful post request")  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/course.html", {
                "courseform": course_form,
            })

    return render(request, "learn/course.html", {
        "courseform": courseform()
    })


def section(request):
    if request.method == 'POST':
        section_form = sectionform(request.POST)

        # The following will take place when the form IS valid
        if section_form.is_valid():
            section_form.save()
            # return validatedates(request, course_form)
            return HttpResponse("you have made a successful post request")  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/section.html", {
                "sectionform": section_form,
            })

    return render(request, "learn/section.html", {
        "sectionform": sectionform()
    })


def lecture(request):
    if request.method == 'POST':
        lecture_form = lectureform(request.POST)

        # The following will take place when the form IS valid
        if lecture_form.is_valid():
            lecture_form.save()
            # return validatedates(request, course_form)
            return HttpResponse("you have made a successful post request")  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/lecture.html", {
                "lectureform": lecture_form,
            })

    return render(request, "learn/lecture.html", {
        "lectureform": lectureform()
    })


def attendance(request):
    if request.method == 'POST':
        attendance_form = attendanceform(request.POST)

        # The following will take place when the form IS valid
        if attendance_form.is_valid():
            attendance_form.save()
            # return validatedates(request, course_form)
            return HttpResponse("you have made a successful post request")  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/attendance.html", {
                "attendanceform": attendance_form,
            })

    return render(request, "learn/attendance.html", {
        "attendanceform": attendanceform()
    })


def lecturenote(request):
    if request.method == 'POST':
        lecturenote_form = lecturenoteform(request.POST)

        # The following will take place when the form IS valid
        if lecturenote_form.is_valid():
            lecturenote_form.save()
            # return validatedates(request, course_form)
            return HttpResponse("you have made a successful post request")  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/lecturenote.html", {
                "lecturenoteform": lecturenote_form,
            })

    return render(request, "learn/lecturenote.html", {
        "lecturenoteform": lecturenoteform()
    })



def comment(request):
    comment_form = commentform(request.POST or None)
    if request.method == 'POST':
        comment_form = commentform(request.POST)

        # The following will take place when the form IS valid
        if comment_form.is_valid():
            comment_form.save()
            # return validatedates(request, course_form)
            return HttpResponse("you have made a successful post request")  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/comment.html", {
                "commentform": comment_form,
            })

    return render(request, "learn/comment.html", {
                "commentform": comment_form,
            })


def assignment(request):
    assignment_form = assignmentform(request.POST or None)

    if request.method == 'POST':
        assignment_form = assignmentform(request.POST)

        # The following will take place when the form IS valid
        if assignment_form.is_valid():
            assignment_form.save()
            # return validatedates(request, course_form)
            return HttpResponse("you have made a successful post request")  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/assignment.html", {
                "assignmentform": assignment_form,
            })

    return render(request, "learn/assignment.html", {
                "assignmentform": assignment_form,
            })


def submission(request):
    submission_form = submissionform(request.POST or None)

    if request.method == 'POST':
        submission_form = submissionform(request.POST)

        # The following will take place when the form IS valid
        if submission_form.is_valid():
            submission_form.save()
            # return validatedates(request, course_form)
            return HttpResponse("you have made a successful post request")  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/submission.html", {
                "submissionform": submission_form,
            })

    return render(request, "learn/submission.html", {
                "submissionform": submission_form,
            })


def mark(request):
    mark_form = markform(request.POST or None)

    if request.method == 'POST':
        mark_form = markform(request.POST)

        # The following will take place when the form IS valid
        if mark_form.is_valid():
            mark_form.save()
            # return validatedates(request, course_form)
            return HttpResponse("you have made a successful post request")  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/mark.html", {
                "markform": mark_form,
            })

    return render(request, "learn/mark.html", {
                "markform": mark_form,
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
        

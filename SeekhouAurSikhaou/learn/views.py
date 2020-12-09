from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError
from django.utils import timezone


from .models import User, Course, Section, Lecture, Attendance, Lecture_Note, Comment, Assignment, Submission, Mark
from .forms import userform, courseform, sectionform, lectureform, attendanceform, lecturenoteform, commentform, assignmentform, submissionform, markform
from .helpers import validateusers
# , validatedates

# Create your views here.



@login_required(login_url='login')
def index(request):
    if request.user.is_staff:
        return HttpResponseRedirect(reverse('admin'))
    else:
        return render(request, "learn/index.html")
        
        # if request.user.type == 'TEACHER':
        #     return render(request, "learn/index.html")



@login_required(login_url='login')
def admin(request):
    return render(request, "learn/admin.html")


@login_required(login_url='login')
def user(request):

    user_form = userform(request.POST or None)

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
            return render(request, "learn/user.html", {
                "userform": user_form
            })
        
    # The following gets rendered when the client sends a GET request to the 'home/' route
    return render(request, "learn/user.html", {
        "userform":user_form,
    })


@login_required(login_url='login')
def courses(request):
    Courses_objects = Course.objects.filter(Status=True)
    print(type(Courses_objects))
    # return HttpResponse(f'{Courses_objects} - {len(Courses_objects)}')
    return render(request, "learn/sections.html", {
        "courses": Courses_objects
    })
    

@login_required(login_url='login')
def course(request, course_id):
    activesections = Section.objects.filter(course_id = course_id, status = True)
    archivedsections = Section.objects.filter(course_id = course_id, status = False)
    current_course = Course.objects.get(pk = course_id)
    return render(request, "learn/section.html", {
        "activesections": activesections,
        "archivedsections":archivedsections,
        "course": current_course

    })
    # return HttpResponse(f"id is {course_id}")


@login_required(login_url='login')
def course_add(request):
    if request.method == 'POST':
        course_form = courseform(request.POST)

        # The following will take place when the form IS valid
        if course_form.is_valid():
            course_form.save()
            # return validatedates(request, course_form)
            return HttpResponseRedirect(reverse('index'))  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/courseadd.html", {
                "courseform": course_form,
            })

    return render(request, "learn/courseadd.html", {
        "courseform": courseform()
    })


@login_required(login_url='login')
def section(request, section_id):
    current_section = Section.objects.get(pk = section_id)
    assignments = Assignment.objects.filter(section_id = section_id)
    lectures = Lecture.objects.filter(section_id = section_id)
    return render(request, "learn/section_view.html", {
        "assignments": assignments,
        "lectures": lectures,
        "section": current_section

    })



@login_required(login_url='login')
def section_add(request):
    if request.method == 'POST':
        section_form = sectionform(request.POST)

        # The following will take place when the form IS valid
        if section_form.is_valid():
            section_form.save()
            # return validatedates(request, course_form)
            return HttpResponseRedirect(reverse('index')) 

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/sectionadd.html", {
                "sectionform": section_form,
            })

    return render(request, "learn/sectionadd.html", {
        "sectionform": sectionform()
    })

@login_required(login_url='login')
def lecture_add(request):
    if request.method == 'POST':
        lecture_form = lectureform(request.POST)

        # The following will take place when the form IS valid
        if lecture_form.is_valid():
            lecture_form.save()
            # return validatedates(request, course_form)
            return HttpResponseRedirect(reverse('index')) 

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/lecture.html", {
                "lectureform": lecture_form,
            })

    return render(request, "learn/lecture.html", {
        "lectureform": lectureform()
    })

@login_required(login_url='login')
def attendance(request):
    if request.method == 'POST':
        attendance_form = attendanceform(request.POST)

        # The following will take place when the form IS valid
        if attendance_form.is_valid():
            attendance_form.save()
            # return validatedates(request, course_form)
            return HttpResponseRedirect(reverse('index'))  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/attendance.html", {
                "attendanceform": attendance_form,
            })

    return render(request, "learn/attendance.html", {
        "attendanceform": attendanceform()
    })

@login_required(login_url='login')
def lecturenote_add(request):
    if request.method == 'POST':
        lecturenote_form = lecturenoteform(request.POST)

        # The following will take place when the form IS valid
        if lecturenote_form.is_valid():
            lecturenote_form.save()
            # return validatedates(request, course_form)
            return HttpResponseRedirect(reverse('index'))  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/lecturenote.html", {
                "lecturenoteform": lecturenote_form,
            })

    return render(request, "learn/lecturenote.html", {
        "lecturenoteform": lecturenoteform()
    })


@login_required(login_url='login')
def comment_add(request):
    comment_form = commentform(request.POST or None)
    if request.method == 'POST':
        comment_form = commentform(request.POST)

        # The following will take place when the form IS valid
        if comment_form.is_valid():
            comment_form.save()
            # return validatedates(request, course_form)
            return HttpResponseRedirect(reverse('index')) 

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/comment.html", {
                "commentform": comment_form,
            })

    return render(request, "learn/comment.html", {
                "commentform": comment_form,
            })


@login_required(login_url='login')
def assignment_view(request):
    current_user = request.user
    sections = Section.objects.get(student = current_user)

    assignments = Assignment.objects.filter(section_id = sections.id)
    return render(request, "learn/assignment_view.html", {
                "assignments": assignments
            })



@login_required(login_url='login')
def assignment_add(request):
    assignment_form = assignmentform(request.POST or None)

    if request.method == 'POST':
        assignment_form = assignmentform(request.POST)

        # The following will take place when the form IS valid
        if assignment_form.is_valid():
            assignment_form.save()
            # return validatedates(request, course_form)
            return HttpResponseRedirect(reverse('index'))  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/assignment.html", {
                "assignmentform": assignment_form,
            })

    return render(request, "learn/assignment.html", {
                "assignmentform": assignment_form,
            })

@login_required(login_url='login')
def submission_add(request):
    submission_form = submissionform(request.POST or None)

    if request.method == 'POST':
        submission_form = submissionform(request.POST)

        # The following will take place when the form IS valid
        if submission_form.is_valid():
            submission_form.save()
            # return validatedates(request, course_form)
            return HttpResponseRedirect(reverse('index'))  

        # The following will take place when the form is NOT valid
        else:
            return render(request, "learn/submission.html", {
                "submissionform": submission_form,
            })

    return render(request, "learn/submission.html", {
                "submissionform": submission_form,
            })



@login_required(login_url='login')
def submission_view(request):
    current_user = request.user
    submissions = Submission.objects.filter(teacher = current_user)
    return render(request, "learn/submission_view.html", {
                "submissions": submissions
            })


@login_required(login_url='login')
def mark_view(request):
    current_user = request.user
    marks = Mark.objects.filter(student = current_user)
    return render(request, "learn/mark_view.html", {
                "marks": marks
            })



@login_required(login_url='login')
def mark_add(request):
    mark_form = markform(request.POST or None)

    if request.method == 'POST':
        mark_form = markform(request.POST)

        # The following will take place when the form IS valid
        if mark_form.is_valid():
            mark_form.save()
            # return validatedates(request, course_form)
            return HttpResponseRedirect(reverse('index'))  

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
        username = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        age = request.POST["age"]
        grade_level = request.POST["grade_level"]
        gender = request.POST["gender"]
        type = request.POST["type"]
        if type == "ADMIN":
            is_staff = True
        else:
            is_staff = False
        
        if type == 'STUDENT':
            parent_id = request.POST["parent_id"]
        else:
            parent_id = None
        
        is_teacher = request.POST['is_teacher']
        is_student = request.POST['is_student']
        # parent_selected = request.POST["parent_id"]
        # print(f"{parent_selected}")

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "learn/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            # user = User.objects.create_user(email, email, password, first_name, username, last_name, age, grade_level, type, is_staff)
            # user = User.objects.create(email, password, first_name, username, last_name, age, grade_level, type, is_staff)
            user = User.objects.create_user(email, email, password)
            user.save()
            latest_user = User.objects.all().latest('id')
            try:
                latest_user.first_name = first_name
                latest_user.last_name = last_name
                latest_user.age = age
                latest_user.type = gender
                latest_user.type = type
                latest_user.grade_level = grade_level
                latest_user.is_staff = is_staff
                # latest_user.date_joined = str(timezone.now)
                latest_user.parent_id = parent_id
                latest_user.is_teacher = is_teacher
                latest_user.save()
            except (TypeError, NameError) as e:
                return render(request, "learn/register.html", {
                    "message": e
                })

        except IntegrityError as e:
            print(e)
            return render(request, "learn/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        parents = User.objects.filter(type='PARENT')
        return render(request, "learn/register.html", {
            "parents": parents
        })
        

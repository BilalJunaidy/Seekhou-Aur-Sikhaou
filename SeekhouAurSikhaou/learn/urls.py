from django.urls import path

from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("course/", views.course, name="course"),
    path("section/", views.section, name="section"),
    path("lecture/", views.lecture, name="lecture"),
    path("attendance/", views.attendance, name="attendance"),
    path("lecturenote/", views.lecturenote, name="lecturenote"),
    path("comment/", views.comment, name="comment"),
    path("assignment/", views.assignment, name="assignment"),
    path("submission/", views.submission, name="submission"),
    path("mark/", views.mark, name="mark"),
]


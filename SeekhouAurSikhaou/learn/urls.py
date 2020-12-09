from django.urls import path

from . import views

urlpatterns = [
    path("admin/", views.admin, name="admin"),
    path("admin/Create_User", views.user, name="admin_create_user"),
    path("admin/Create_Course", views.course_add, name="admin_create_course"),
    path("admin/Create_Section", views.section, name="admin_create_section"),

    path("home", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("courses/", views.courses, name="courses"),
    path("sections/<int:course_id>", views.course, name="sections"),
    path("courses/add", views.course_add, name="course_add"),
    path("section/<str:section_id>", views.section, name="section"),
    path("section/add", views.section_add, name="section_add"),
    path("lecture/", views.lecture, name="lecture"),
    path("attendance/", views.attendance, name="attendance"),
    path("lecturenote/", views.lecturenote, name="lecturenote"),
    path("comment/", views.comment, name="comment"),
    path("assignment/", views.assignment, name="assignment"),
    path("submission/", views.submission, name="submission"),
    path("mark/", views.mark, name="mark"),
]


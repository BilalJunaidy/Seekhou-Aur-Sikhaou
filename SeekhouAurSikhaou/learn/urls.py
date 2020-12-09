from django.urls import path

from . import views

urlpatterns = [
    path("admin/", views.admin, name="admin"),
    path("admin/Create_User", views.user, name="admin_create_user"),
    path("admin/Create_Course", views.course_add, name="admin_create_course"),
    path("admin/Create_Section", views.section_add, name="admin_create_section"),

    path("home", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("courses/", views.courses, name="courses"),
    path("sections/<int:course_id>", views.course, name="sections"),
    path("courses/add", views.course_add, name="course_add"),
    path("section/<str:section_id>", views.section, name="section"),
    path("section/add", views.section_add, name="section_add"),
    path("lecture/add", views.lecture_add, name="create_lecture"),
    path("attendance/", views.attendance, name="attendance"),
    path("lecturenote/add", views.lecturenote_add, name="create_lecturenote"),
    path("comment/add", views.comment_add, name="create_comment"),
    path("assignment/add", views.assignment_add, name="create_assignment"),
    path("assignment/view", views.assignment_view, name="view_assignment"),
    path("submission/add", views.submission_add, name="create_submission"),
    path("submission/view", views.submission_view, name="view_submission"),
    path("mark/add", views.mark_add, name="create_mark"),
    path("mark/view", views.mark_view, name="view_mark"),
]


from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage),
    path('homepage', views.homepage),
    path('logout', views.logout),
    path('student_login', views.student_login),
    path('student_signin', views.student_signin),
    path('teacher_login', views.teacher_login),
    path('student_branches', views.student_branches),
    path('teacher_branches', views.teacher_branches),
    path('teacher_signin', views.teacher_signin),
    path('student_lectures_list', views.student_lectures_list),
    path('teachers_lectures_list', views.teachers_lectures_list),
    path('search', views.search),
    path('student_subjects', views.student_subjects),
    path('teacher_subjects', views.teacher_subjects),
    path('student_sem', views.student_sem),
    path('teacher_sem', views.teacher_sem),
    path('student_videolecture', views.student_videolecture),
    path('teacher_videolecture', views.teacher_videolecture),
    path('confirm', views.confirm),
]
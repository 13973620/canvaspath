# coding:utf-8
# life is short, you need Python！

from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('enroll/', views.enroll_student, name='enroll'),
    path('assign/', views.assign_prof, name='assign'),
    path('create_hw/', views.create_hw, name='create_hw'),
    path('create_exam/', views.create_exam, name='create_exam'),
    path('create_hw_grade/', views.create_hw_grade, name='create_hw_grade'),
    path('create_exam_grade/', views.create_exam_grade, name='create_exam_grade'),
    path('add_course/', views.manage_course, name='add_course'),
    path('hw_change/', views.hw_change, name='hw_change'),
    path('grade_change/', views.grade_change, name='grade_change'),
]

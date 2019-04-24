# coding:utf-8
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    # path('blank/', views.blank, name='blank'),
    # path('data_fresh/', views.data_fresh, name="data_fresh"),
    # path('response_timemap/', views.response_timemap, name="response_timemap"),
    # path('settings/', views.settings, name='settings'),
]

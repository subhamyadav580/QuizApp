from unicodedata import name
from django.contrib import admin
from django.urls import path
from quizApp.views import (
    AddSubject,
    register,
)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', register, name='register'),
    path('login', obtain_auth_token, name='login'),
    path('addsubject', AddSubject, name='addsubject')
]

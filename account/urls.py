import imp
from django.contrib import admin
from django.urls import path, include
from .views import (
    UserListAPI,
    UserDetailAPI
)

urlpatterns = [
    path('userlist/', UserListAPI.as_view()),
    path('userdetail/<int:pk>/' , UserDetailAPI.as_view())

]
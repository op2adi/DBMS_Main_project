from django.contrib import admin
from django.urls import path
from makemytrip import views

urlpatterns = [
    path('',views.login_view),
    # path('login_view/', views.login_view, name='login_view'),
]

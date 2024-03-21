from django.contrib import admin
from django.urls import path
from makemytrip import views

urlpatterns = [
    path('',views.login_view),
    path('create_account/', views.create_account, name='create_account'),
    path('Flights.html',views.Flights, name='flights'),
    # path('login_view/', views.login_view, name='login_view'),
]

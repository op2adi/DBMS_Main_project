import secrets
import string

from django.contrib import admin
from django.urls import path
from makemytrip import views


def generate_random_word(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))
urlpatterns = [
    path('',views.login_view),
    path('create_account/', views.create_account, name='create_account'),
    path('Flights/',views.Flights, name='Flights'),
    # path('login_view/', views.login_view, name='login_view'),
    path('Trains/',views.Trains,name='Trains'),
    path('Hotels/',views.Hotels, name='Hotels'),
    path('Holidays/',views.Holidays, name='Holidays'),
    path('trains_search',views.search_trains, name='search_trains'),
    path('Book/',views.Book_full, name='Book_full'),
    path('submit_book',views.submit_booking, name='submit_book'),
    path('payments/',views.Payment, name='payments'),
    path('home/',views.home_spl, name='home'),
    path('Tickets/',views.Tickets, name='Tickets'),
    path(generate_random_word(32)+'/',views.spl_comm, name='spl_comm'),
]

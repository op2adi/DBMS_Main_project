"""
URL configuration for Tripsync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# URL configuration for Tripsync project.

from django.contrib import admin
from django.urls import path
from makemytrip import views
from makemytrip.views import login_view  # Correct import statement
from makemytrip.views import (Book_full, Flights, Holidays, Hotels, Trains,
                              create_account, search_trains)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_account/', create_account, name='create_account'),
    path('', login_view, name='login'),  # Corrected URL pattern
    path('Flights/',Flights, name='Flights'),
    path('Trains/',Trains,name='Trains'),
    path('Hotels/',Hotels, name='Hotels'),
    path('Holidays/',Holidays, name='Holidays'),
    path('trains_search',search_trains, name='search_trains'),
    path('Book/',Book_full, name='Book_full'),
    path('submit_book/',views.submit_booking, name='submit_booking'),
    path('payments/',views.Payment, name='payments'),
]

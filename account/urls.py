from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('myroom/', myroom, name='myroom'),
    path('login/', login, name='login'),
    path(r'^logout/$', logout, name='logout'),
    path('register/startupper/', registerUserStartupper, name='registerUserStartupper'),
    path('register/investor/', registerUserInvestor, name='registerUserInvestor'),
    path('aboutus/', aboutus, name='about_us'),
]
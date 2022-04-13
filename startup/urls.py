from django.urls import path
from .views import *

urlpatterns = [
    path('', startups, name='startups'),
    path('add_startup/', add_startup, name='add_startup'),
    path('replenish_the_balance/', replenish_the_balance, name='replenish_the_balance'),
    path('project/<int:pk>', startup_page, name='project'),
]
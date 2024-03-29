from django.urls import path
from .views import *

urlpatterns = [
    path('', startups, name='startups'),
    path('my/', my_startups, name='my_startups'),
    path('add_startup/', add_startup, name='add_startup'),
    path('replenish_the_balance/', replenish_the_balance, name='replenish_the_balance'),
    path('invest_startup/<int:pk>', invest_startup, name='invest_startup'),
    path('project/<int:pk>', startup_page, name='project'),
]
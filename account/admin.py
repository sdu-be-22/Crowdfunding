from django.contrib import admin
from account.models import UserInvestor, UserStartupper
from startup.models import *


admin.site.register(Startup)
admin.site.register(UserInvestor)
admin.site.register(UserStartupper)

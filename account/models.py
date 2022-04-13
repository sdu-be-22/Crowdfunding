from django.db import models
from django.contrib.auth.models import User


class UserInvestor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birth_date = models.DateField()
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    current_money = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user.username


class UserStartupper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birth_date = models.DateField()
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.user.username

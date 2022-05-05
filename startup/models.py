from django.urls import reverse

from account.models import *
from django.db import models


class Startup(models.Model):
    startupper = models.ForeignKey(UserStartupper, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    initial_capital = models.IntegerField()
    accumulated_capital = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to="images/")


    categories = [
        ('IT', 'IT'),
        ('Ecology', 'Ecology'),
        ('Electronic', 'Electronic'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Gaming', 'Gaming'),
        ('Small Business', 'Small Business'),
        ('Other', 'Other')
    ]
    category = models.CharField(max_length=20, choices=categories, default='Other')


    def __str__(self):
        return self.title

    def percentage(self):
        return float('{:.1f}'.format(self.accumulated_capital * 100 / self.initial_capital))

    def s_name(self):
        s = UserStartupper.objects.get(id = self.startupper_id)
        return s.user.username

    def get_absolute_url(self):
        return reverse('project', kwargs={'startup_id': self.pk})


class Investing(models.Model):
    investor = models.ForeignKey(UserInvestor, on_delete=models.CASCADE)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    investment_amount = models.IntegerField()
    investment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.startup.title
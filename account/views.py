from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from account.forms import *
from startup.models import *
from account.models import *

def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'not logged in'

    context = {'username': username}
    return render(request, 'index.html', context=context)


def myroom(request):
    if request.user.is_authenticated:
        is_authenticated = True
        user = request.user
        user_id = request.user.id
        startupper = UserStartupper.objects.get(user_id=user_id)
        startup_list = Startups.objects.filter(startupper_id=startupper.pk)
        startup_count = len(startup_list)
        last_startup_list = startup_list.order_by('-id')[:3]

    context = {
        'user': user,
        'is_authenticated': is_authenticated,
        'startupper': startupper,
        'startup_list': last_startup_list,
        'startup_count': startup_count
    }
    return render(request, 'my_room_startupper.html', context=context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth.logout(request)

    url = '/'
    return HttpResponseRedirect(url)


def registerUserInvestor(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        investor_form = UserInvestorForm(request.POST)

        if form.is_valid() and investor_form.is_valid():
            user = form.save()
            investor = investor_form.save(commit=False)
            investor.user = user

            investor.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth.login(request, user)

            return redirect('index')
    else:
        form = ExtendedUserCreationForm()
        investor_form = UserInvestorForm()

    context = {'form': form, 'startupper_form': investor_form}

    return render(request, 'register_startupper.html', context)


def registerUserStartupper(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        startupper_form = UserStartupperForm(request.POST)

        if form.is_valid() and startupper_form.is_valid():
            user = form.save()
            startupper = startupper_form.save(commit=False)
            startupper.user = user

            startupper.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth.login(request, user)

            return redirect('index')
    else:
        form = ExtendedUserCreationForm()
        startupper_form = UserStartupperForm()

    context = {'form': form, 'startupper_form': startupper_form}

    return render(request, 'register_startupper.html', context)



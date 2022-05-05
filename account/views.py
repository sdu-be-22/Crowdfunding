from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from account.forms import *
from startup.models import *
from account.models import *

def index(request):
    query = "SELECT * FROM startup_startup ORDER by initial_capital, accumulated_capital DESC"
    startup = Startup.objects.raw(query)[0]
    investor = UserInvestor.objects.order_by('-current_money')[0]
    context = {
        'startup': startup,
        'investor': investor
    }
    return render(request, 'main_page.html', context=context)



def myroom(request):
    if request.user.is_authenticated:
        is_authenticated = True
        user = request.user
        user_id = request.user.id
        if UserStartupper.objects.filter(user_id=user_id).exists():
            person = UserStartupper.objects.get(user_id=user_id)
            startup_list = Startup.objects.filter(startupper_id=person.pk)
            startup_count = len(startup_list)
            last_startup_list = startup_list.order_by('-id')[:3]
            user_type = "startupper"
            form = AddStartup()
        else:
            person = UserInvestor.objects.get(user_id=user_id)
            # startup_list = Startup.objects.filter(investor=person)
            sql_query = "SELECT startup_investing.id as id, startup_startup.title, startup_startup.description, startup_id as pk, image FROM startup_startup JOIN startup_investing ON startup_startup.id = startup_investing.startup_id WHERE startup_investing.investor_id = %s ORDER BY id DESC;" % person.id
            startup_list = Startup.objects.raw(sql_query)
            startup_count = len(startup_list)
            last_startup_list = startup_list[:3]
            user_type = "investor"
            form = 0

    context = {
        'user': user,
        'is_authenticated': is_authenticated,
        'person': person,
        'startup_list': last_startup_list,
        'startup_count': startup_count,
        'user_type': user_type,
        'form': form
    }
    return render(request, 'my_room.html', context=context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect("/")
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

def aboutus(request):
    return render(request, 'about_us.html')

def investors(request):
    return render(request, 'investors.html')

from django.core.paginator import Paginator, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from startup.models import *
from account.models import *


# Create your views here.
def startups(request):
    if request.user.is_authenticated:
        is_authenticated = True
        username = request.user.username
    else:
        is_authenticated = False
        username = 'not logged in'

    page = 0
    paginator = 0
    startup_list = Startup.objects.order_by('-pk')
    startuppers = UserStartupper.objects.all()

    page = request.GET.get('page', 1)
    if request.GET.get('filter_category'):
        category = request.GET.get('filter_category')
        collected_amount = request.GET.get('collected_amount')

        startup = 0

        if category == 'All':
            startup = Startup.objects.order_by('-pk')
        else:
            startup = Startup.objects.filter(category=category).order_by('-pk')

        startups = list(startup)

        startup_list = []
        if collected_amount == '1':
            for i in startups:
                startup_list.append(i)
        elif collected_amount == '2':
            for i in startups:
                if i.percentage() > 0:
                    startup_list.append(i)
        elif collected_amount == '3':
            for i in startups:
                if i.percentage() >= 25:
                    startup_list.append(i)
        elif collected_amount == '4':
            for i in startups:
                if i.percentage() >= 50:
                    startup_list.append(i)
        elif collected_amount == '5':
            for i in startups:
                if i.percentage() >= 75:
                    startup_list.append(i)


    paginator = Paginator(startup_list, 5)
    try:
        startup_list = paginator.page(page)
    except PageNotAnInteger:
        startup_list = paginator.page(1)

    context = {
        'startups': startup_list,
        'startuppers': startuppers,
        'is_authenticated': is_authenticated,
        'username': username
    }
    return render(request, 'startups.html', context=context)


def startup_page(request, pk):
    if request.user.is_authenticated:
        is_authenticated = True
        username = request.user.username

        if UserStartupper.objects.filter(user_id=request.user.id).exists():
            is_investor = False
        else:
            is_investor = True

    else:
        is_authenticated = False
        username = 'not logged in'

    startup = Startup.objects.get(pk=pk)

    context = {
        'project': startup,
        'is_authenticated': is_authenticated,
        'is_investor': is_investor,
        'username': username
    }
    return render(request, 'startup.html', context=context)


def add_startup(request):
    user_id = request.user.id
    startupper = UserStartupper.objects.get(user_id=user_id)
    title = request.POST.get('title')
    description = request.POST.get('description')
    category = request.POST.get('category')
    initial_capital = request.POST.get('initial_capital')
    image = request.POST.get('image')

    startupper.startups_set.create(
        title=title,
        description=description,
        category=category,
        initial_capital=initial_capital,
        accumulated_capital=0
    )

    this_startup = Startup.objects.order_by('-pk')[0]
    url = '/startups/project/' + str(this_startup.pk)
    return HttpResponseRedirect(url)

def replenish_the_balance(request):
    user_id = request.user.id
    investor = UserInvestor.objects.filter(user_id=user_id)
    amount = request.POST['amount']
    new_amount = investor[0].current_money + int(amount)
    investor.update(current_money = new_amount)
    return redirect('myroom')

def invest_startup(request, pk):
    user_id = request.user.id
    investor = UserInvestor.objects.filter(user_id=user_id)

    startup = Startup.objects.get(pk=pk)
    print(startup.initial_capital)

    if request.method == 'POST':
        amount = int(request.POST['amount'])
        accumulated_capital = startup.accumulated_capital
        investor_money = investor[0].current_money

        if amount > investor_money:
            print("You don't have enough money")
        else:
            new_amount = accumulated_capital + amount
            Startup.objects.filter(id=startup.id).update(accumulated_capital=new_amount)
            investor.update(current_money=investor_money - amount)

    url = '/startups/project/' + str(pk)
    return HttpResponseRedirect(url)
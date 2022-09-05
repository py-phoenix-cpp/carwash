from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *



@login_required(login_url='login')
def Index(request):
    context = {
        'bonus_bor': Client.objects.filter(bonus__gt=0).order_by('-id'),
        'client_soni': Client.objects.all().count()
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def Clients(request):
    context = {
        'bonus_bor': Client.objects.filter(bonus__gt=0).order_by('-id'),
        'client_soni': Client.objects.all().count()
    }
    return render(request, 'clients.html', context)


@login_required(login_url='login')
def addClientView(request):
    a = 0
    if request.method == 'POST':
        name = request.POST.get('name')
        car_number = request.POST.get('car_number')
        price = request.POST.get('price')
        have = Client.objects.filter(car_number=car_number)
        if have.count() > 0:
            a = 1
        else:
            Client.objects.create(
                name=name,
                car_number=car_number,
                price=price,
                quantity=1,
            )
    context = {
        'a': a
    }
    return render(request, 'add-client.html', context)


def PagenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list


@login_required(login_url='login')
def listClientsView(request):
    obj = Client.objects.all()
    context = {
        'list': Client.objects.all().order_by('-id'),
        'objects': PagenatorPage(obj, 8, request)
    }
    return render(request, 'list-clients.html', context)


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        users = User.objects.filter(username=username)
        if users.count() > 0:
            usr = authenticate(username=username, password=password)
            if usr is not None:
                login(request, usr)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return redirect('login')
    return render(request, 'login.html')


def LogoutView(request):
    logout(request)
    return redirect('login')


# def test():
#     discond = Discond.objects.create(
#         all_sum = 200,
#         quantity = 2
#     )
#     client = Client.objects.get(id=2)
#     cliend.price += discond.all_sum
#     cliend.quantity += discond.quantity
#     cliend.save()

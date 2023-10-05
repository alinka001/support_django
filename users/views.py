from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from tickets.models import Ticket
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import conf
from .forms import CustomUserCreationForm
from .forms import *


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tickets-all')
        else:
            return render(request, 'users/login.html', )
    else:
        return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'Вы вышли из учетной записи')
    return redirect('login')


def registerUser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Аккаунт успешно создан!')

            login(request, user)
            return redirect('login')

        else:
            messages.success(
                request, 'Во время регистрации возникла ошибка')

    context = {'form': form}
    return render(request, 'users/register.html', context)



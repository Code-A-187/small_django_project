from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def register(request):
    form = UserCreationForm
    return render(request, 'users/register.html', {'form': form})

def login(request):
    return render(request, 'users/login.html')
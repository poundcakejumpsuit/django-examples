from django.shortcuts import render, redirect
from django.views import generic
from .models import User
# from .forms import LoginForm, UserForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

# @login_required(login_url="login/")
def home(request):
    return render(request, 'home.html')
from django.shortcuts import render, redirect
from django.views import generic
from .models import User
from .forms import LoginForm, UserForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required(login_url="login/")
def home(request):
    return render(request, 'home.html')

class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('tadu_server:home')
    template_name = 'login.html'
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('tadu_server:home')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})
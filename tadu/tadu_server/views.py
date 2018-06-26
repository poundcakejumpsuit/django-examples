from django.shortcuts import render, redirect
from django.views import generic
from .models import User, Task
from .forms import LoginForm, UserForm, TaskForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string

def index(request):
    return render(request, 'index.html')

@login_required(login_url="tadu_server:login")
def home(request):
    return render(request, 'home.html')

class HomeView(generic.detail.DetailView):
    template_name = 'home.html'
    model = User
    context_object_name = 'user_tasks'

    def get_object(self):
        return Task.objects.filter(task_owner=self.request.user)

class LoginView(generic.FormView):
    form_class = LoginForm
    # success_url = reverse_lazy('tadu_server:home_tasks', kwargs={'username' : username})

    template_name = 'login.html'
    def form_valid(self, form):
        self.form = form
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        cur_user = self.form.cleaned_data['username']
        return reverse_lazy('tadu_server:home_tasks', kwargs={'username': cur_user})

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
            # return super(LoginView, self).form_valid(form)
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "add_task.html"

    def dispatch(self, *args, **kwargs):
        print(kwargs)
        self.task_id = kwargs['pk']
        return super(TaskUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        task = Task.objects.get(pk=self.task_id)
        return redirect('tadu_server:home')
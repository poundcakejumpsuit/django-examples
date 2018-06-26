from django.urls import path
from . import views
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

app_name = 'tadu_server'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', login_required(views.home), name='home'),
    path('login/', views.LoginView.as_view(), {'next_page' : 'tadu_server:home_tasks'}, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', logout, {'next_page' : 'tadu_server:login'}, name='logout'),
    path('home/<slug:username>', login_required(views.HomeView.as_view()), name='home_tasks'),
    path('home/<slug:username>/add_task', login_required(views.TaskUpdateView.as_view()), {'next_page' : 'tadu_server:home_tasks'}, name='add_task'),
]

from django.urls import path
from . import views
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

app_name = 'tadu_server'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', logout, {'next_page' : 'tadu_server:login'}, name='logout'),

]

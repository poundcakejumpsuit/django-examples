from django import forms
from django.contrib.auth.models import User
from .models import User, Task
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('task_owner', 'task_text', 'entry_date', 'due_date')
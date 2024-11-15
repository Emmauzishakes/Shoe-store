from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CreateUser(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus ':'True','class': 'form-control w-50 p-2'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus ':'True','class': 'form-control w-50 p-2'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus ':'True','class': 'form-control w-50 p-2'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control w-50 p-2'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control w-50 p-2'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control w-50 p-2'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-50 p-2'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control w-50 p-2'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control w-50 p-2'}))

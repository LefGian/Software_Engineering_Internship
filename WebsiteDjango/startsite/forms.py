from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User    # define with wich model to interact
        # specify form fields that are displayed, and order of them
        fields = ['username', 'password1', 'password2', 'groups']
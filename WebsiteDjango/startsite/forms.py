from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """Form used to Register a User wich is stored in User-DB-Model

    :param UserCreationForm: Inherits from the ModelForm from Django
    :type UserCreationForm: form
    """
    class Meta:
        model = User    # define with wich model to interact
        # specify form fields that are displayed, and order of them
        fields = ['username', 'password1', 'password2', 'groups']
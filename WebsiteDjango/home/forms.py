from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TODO(UserCreationForm):
    class Meta:
        model = User  # define with wich model to interact
        # specify form fields that are displayed, and order of them
        fields = []

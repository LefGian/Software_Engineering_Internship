from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    """Form used to Update the User Information wich is stored in User-DB-Model

    :param forms: Inherits from the ModelForm from Django
    :type forms: form
    """
    class Meta:
        model = User    # works with the User - Model
        fields = ['username', 'first_name', 'last_name']    # Fields we want to Update

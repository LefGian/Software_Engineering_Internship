"""
views.py for register and login

Register POST
{
'csrfmiddlewaretoken': ['NmlHCH7isoW9JkFzTcrfEyMW4kMzYOpwMBR5XY6lM41E66mBnq3tnK6G9GDwqUiL'],
'username':['ffffffffffffffffffff'],
'email':['ffffffffffffffffffff@gmail.com'],
'password1':['testing1234'],
'password2':['testing1234']
}
"""

from atexit import register
from traceback import print_tb
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from utils import utils


def startsite(request):
    show_login_error = 0
    show_register_error = 0
    is_register = 0

    fehlermeldung_login = 'Username or Password wrong'

    if request.method == "POST":  # if we get a post request, initiate form to fillout
        is_register = int(request.POST['jgu-mod-value'])
        #  is_login = request.POST.getlist('jgu-mod-value')[0]
        form_register = UserRegisterForm()
        # if register

        if is_register:

            register_form_dict = {'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
                                  'username': request.POST['jgu-username'],
                                  'password1': request.POST['jgu-password'],
                                  'password2': request.POST['jgu-password-repeat'],
                                  }

            form_register = UserRegisterForm(register_form_dict)

            if form_register.is_valid():
                form_register.save()

                user = authenticate(request, username=register_form_dict['username'], password=register_form_dict['password1'])
                utils.set_group(user, 'Student')

                # user = User.objects.get(username = register_form_dict['username'])
                # user.groups.add()
                return redirect('startsite-startseite')
            show_register_error = 1

        # if login
        else:
            username = request.POST['jgu-username']
            password = request.POST['jgu-password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            show_login_error = 1

    else:  # else empy form
        form_register = UserRegisterForm()

    fehlermeldung_register = form_register.errors.as_data()
    fehlermeldung_register_str_arr = []
    for key in fehlermeldung_register:
        for error_arr in fehlermeldung_register[key]:
            fehlermeldung_register_str_arr += error_arr

    context = {
        'fehlermeldung_register_str_arr': fehlermeldung_register_str_arr,
        'show_register_error': show_register_error,
        'fehlermeldung_login': fehlermeldung_login,
        'show_login_error': show_login_error,
        'is_register': is_register,
    }
    return render(request, 'startsite/startseite.html', context)

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserUpdateForm, User


# Create your views here.

@login_required
def userprofile(request):
    user = request.user
    form_user_update = UserUpdateForm(instance=user)
    form_user_pwd = PasswordChangeForm(request.user)
    print(f'username: {user.username} | userid: {user.id}')
    fehlermeldung_password = ''
    fehlermeldung_user_update_str_arr = []

    if request.method == 'POST':

        password = ''
        password1 = ''
        password2 = ''
        if 'jgu-password' in request.POST:
            password = request.POST['jgu-password']
        if 'jgu-password-new' in request.POST:
            password1 = request.POST['jgu-password-new']
        if 'jgu-password-new-confirm' in request.POST:
            password2 = request.POST['jgu-password-new-confirm']

        user_update_form_dict = {'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
                                 'first_name': request.POST['jgu-vorname'],
                                 'last_name': request.POST['jgu-nachname'],
                                 'username': request.POST['jgu-username'],
                                 }

        user_check = authenticate(request, username=user.username, password=password)
        if user_check is not None:
            print('right pwd')
            form_user_update = UserUpdateForm(user_update_form_dict, instance=request.user)

            if password1:
                user_pwd_update_dict = {
                    'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
                    'old_password': password,
                    'new_password1': password1,
                    'new_password2': password2,
                }

                print(user_pwd_update_dict)

                form_user_pwd = PasswordChangeForm(request.user, user_pwd_update_dict)
                print(f'is pwd change form valid?: {form_user_pwd.is_valid()}')
                if form_user_pwd.is_valid():
                    form_user_pwd.save()
                    update_session_auth_hash(request, request.user)
                    return redirect('userprofile-userprofile')





        else:
            fehlermeldung_password = 'Password Wrong'

        if form_user_update.is_valid():
            form_user_update.save()

            return redirect('userprofile-userprofile')

    fehlermeldung_user_update = form_user_update.errors.as_data()
    fehlermeldung_password_form = form_user_pwd.errors.as_data()
    print(fehlermeldung_user_update)
    if fehlermeldung_password:
        fehlermeldung_user_update_str_arr = [fehlermeldung_password]

    for key in fehlermeldung_user_update:
        for error_arr in fehlermeldung_user_update[key]:
            fehlermeldung_user_update_str_arr += error_arr

    for key in fehlermeldung_password_form:
        for error_arr in fehlermeldung_password_form[key]:
            fehlermeldung_user_update_str_arr += error_arr

    print(fehlermeldung_user_update_str_arr)
    user_group = 'filler'
    show_error = 0
    if fehlermeldung_user_update_str_arr:
        show_error = 1

    context = {
        'form_user_update': form_user_update,
        'user': user,
        'user_group': user_group,
        'fehlermeldung_user_update_str_arr': fehlermeldung_user_update_str_arr,
        'show_error': show_error,
    }
    return render(request, 'userprofile/nutzerprofil.html', context)

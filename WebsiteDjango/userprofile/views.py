from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserUpdateForm
from utils import utils


@login_required
def userprofile(request):
    user = request.user
    error_messages = []
    show_error = 0
    user_update_form = UserUpdateForm(instance=user)
    password_change_form = PasswordChangeForm(user)
    user_group = utils.get_group(user)
    user_group.sort()
    user_group = user_group[0]

    if request.method == 'POST':
        password = request.POST['jgu-password']
        user_update_dict = {
            'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'first_name': request.POST['jgu-vorname'],
            'last_name': request.POST['jgu-nachname'],
            'username': request.POST['jgu-username'],
        }
        user_check = authenticate(request, username=user.username, password=password)

        if user_check is not None:
            user_update_form = UserUpdateForm(user_update_dict, instance=user)
            new_password_entered = request.POST['jgu-password-new'] != ''
            new_password_confirmed = request.POST['jgu-password-new-confirm'] != ''
            if new_password_entered and new_password_confirmed:
                password1 = request.POST['jgu-password-new']
                password2 = request.POST['jgu-password-new-confirm']
                user_password_dict = {
                    'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
                    'old_password': password,
                    'new_password1': password1,
                    'new_password2': password2,
                }

                user_password_form = PasswordChangeForm(user, user_password_dict)
                errors = user_password_form.errors.as_data()
                if errors:
                    for error_key in errors:
                        for error_list in errors[error_key]:
                            for error in error_list:
                                error_messages.append(error)

                if user_password_form.is_valid() and user_update_form.is_valid():
                    user_password_form.save()
                    user_update_form.save()
                    update_session_auth_hash(request, user)
                    return redirect('userprofile-userprofile')
            elif user_update_form.is_valid():
                user_update_form.save()
                return redirect('userprofile-userprofile')
            else:
                errors = user_update_form.errors.as_data()
                for error_key in errors:
                    for error_list in errors[error_key]:
                        for error in error_list:
                            error_messages.append(error)

                errors = password_change_form.errors.as_data()
                for error_key in errors:
                    for error_list in errors[error_key]:
                        for error in error_list:
                            error_messages.append(error)
        else:
            error_messages.append('Wrong password')

    if error_messages:
        show_error = 1

    context = {
        'user': user,
        'error_messages': error_messages,
        'show_error': show_error,
        'user_role': user_group,
    }
    return render(request, 'userprofile/nutzerprofil.html', context)

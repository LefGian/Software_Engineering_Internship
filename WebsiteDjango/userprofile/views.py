from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash
from .forms import UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserUpdateForm, User


@login_required
def userprofile(request):
    user = request.user
    error_messages = []
    show_error = 0
    user_update_form = UserUpdateForm(instance=user)
    password_change_form = PasswordChangeForm(user)

    if request.method == 'POST':

<<<<<<< HEAD
        password = request.POST['jgu-password']
        user_update_dict = {
            'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'first_name': request.POST['jgu-vorname'],
            'last_name': request.POST['jgu-nachname'],
            'username': request.POST['jgu-username'],
        }
=======
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

>>>>>>> main
        user_check = authenticate(request, username=user.username, password=password)

        if user_check is not None:
            user_update_form = UserUpdateForm(user_update_dict, instance=user)
            new_password_entered = 'jgu-password-new' in request.POST
            new_password_confirmed = 'jgu-password-new-confirm' in request.POST
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
<<<<<<< HEAD
            elif user_update_form.is_valid():
                user_update_form.save()
                return redirect('userprofile-userprofile')
            else:
                errors =  user_update_form.errors.as_data()
                for error_key in errors:
                        for error_list in errors[error_key]:
                            for error in error_list:
                                error_messages.append(error)
                
                errors =  password_change_form.errors.as_data()
                for error_key in errors:
                        for error_list in errors[error_key]:
                            for error in error_list:
                                error_messages.append(error)
        else:
            error_messages.append('Wrong password')
    
    if error_messages:
        show_error = 1
    
    context = {
        'user' : user,
        'error_messages' : error_messages,
        'show_error' : show_error,
        'user_role' : 'Student',
=======





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
>>>>>>> main
    }
    return render(request, 'userprofile/nutzerprofil.html', context)

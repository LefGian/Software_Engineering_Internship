from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserUpdateForm
from utils import utils


@login_required
def userprofile(request):
    """Django-View that is used to call userprofile/nutzerprofil.html site

    :param request: HttpRequest request from Django, that delivers all the Information
    :type request: HttpRequest
    :return: render of userprofile/nutzerprofil.html with context Dict
    :rtype: HttpResponse
    """
    user = request.user
    error_messages = [] # Array holding the error messages, later displayed in html
    show_error = 0 # shows if error_messages should be displayed
    user_update_form = UserUpdateForm(instance=user)    # Empty initialize of Form that holds Userinfo
    password_change_form = PasswordChangeForm(user) # Empty initialize of Form that holds PasswordInfo
    user_group = utils.get_group(user)  # get the group of the user 
    user_group.sort()   # sort alphabetically, because we can only display one group
    user_group = user_group[0]
    jgu_save = 0

    if request.method == 'POST':
        jgu_save = request.POST['jgu-save']
        password = request.POST['jgu-password']
        user_update_dict = { # Dict with all the info that we need for the userupdate process
            'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'first_name': request.POST['jgu-vorname'],
            'last_name': request.POST['jgu-nachname'],
            'username': request.POST['jgu-username'],
        }
        user_check = authenticate(request, username=user.username, password=password) # check if username and password is right

        if user_check is not None:  # if it is right try to update the user
            user_update_form = UserUpdateForm(user_update_dict, instance=user)  # fill UpdateForm with data from dict
            new_password_entered = request.POST['jgu-password-new'] != ''
            new_password_confirmed = request.POST['jgu-password-new-confirm'] != ''
            if new_password_entered and new_password_confirmed: # if both fields got filled in Form on Website -> user wants to change password
                # get the new passwords
                password1 = request.POST['jgu-password-new']
                password2 = request.POST['jgu-password-new-confirm']
                user_password_dict = {  # dict with all the info we need for the PasswordChangeForm
                    'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
                    'old_password': password,
                    'new_password1': password1,
                    'new_password2': password2,
                }

                user_password_form = PasswordChangeForm(user, user_password_dict)   # fill Form with info from dict

                # get Errors and append them to error_messages
                errors = user_password_form.errors.as_data()
                if errors:
                    for error_key in errors:
                        for error_list in errors[error_key]:
                            for error in error_list:
                                error_messages.append(error)

                # check if the PasswordUpdateForm was filled with correct data, if yes safe changes to DB
                if user_password_form.is_valid() and user_update_form.is_valid():
                    user_password_form.save()
                    user_update_form.save()
                    update_session_auth_hash(request, user)
                    # redirect user to the Profile page and show that change was successful (done with parameters)
                    return render(request, 'userprofile/nutzerprofil.html', {'jgu_save': 1, 'show_error' : 0, 'user_role' : user_group,})
            
            # check if UserUpdateForm was filled with correct data, if yes safe changes to DB
            elif user_update_form.is_valid():
                user_update_form.save()
                 # redirect user to the Profile page and show that change was successful (done with parameters)
                return render(request, 'userprofile/nutzerprofil.html', {'jgu_save': 1, 'show_error' : 0, 'user_role' : user_group,})
            
            # get Errors and append them to error_messages
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
        
        else: # user authentification failed -> user entered wrong password
            error_messages.append('Wrong password')

    if error_messages: # if there are entries in the error_messages array -> display them
        show_error = 1

    context = { # pass info variables to html
        'user' : user,
        'error_messages' : error_messages,
        'show_error' : show_error,
        'user_role' : user_group,
        'jgu_save': jgu_save, 
    }
    return render(request, 'userprofile/nutzerprofil.html', context)

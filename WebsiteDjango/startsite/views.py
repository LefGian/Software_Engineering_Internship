from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from utils import utils
from .forms import UserRegisterForm


def startsite(request):
    """Django-View that is used to call startseite.html site
    handels Login and Regiser Functionality

    :param request: HttpRequest request from Django, that delivers all the Information
    :type request: HttpRequest
    :return: render of startsite/startseite.html with context Dict
    :rtype: HttpResponse
    """   
    show_login_error = 0
    show_register_error = 0
    is_register = 0

    fehlermeldung_login = 'Username or Password wrong'

    if request.method == "POST":  # if we get a post request, initiate form to fillout
        is_register = int(request.POST['jgu-mod-value'])
        form_register = UserRegisterForm()

        if is_register: # if register form is popped up on site
            register_form_dict = { # Dict with all the info we need for the Registerform
                                  'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
                                  'username': request.POST['jgu-username'],
                                  'password1': request.POST['jgu-password'],
                                  'password2': request.POST['jgu-password-repeat'],
                                  }

            form_register = UserRegisterForm(register_form_dict) # fill Form with data

            # check if the UserRegisterForm was filled with correct data, if yes safe new user in DB
            if form_register.is_valid():
                form_register.save()

                user = authenticate(request,
                                    username=register_form_dict['username'],
                                    password=register_form_dict['password1'])
                utils.set_group(user, 'Student') # set Group to Student (default)

                return redirect('startsite-startseite')
            show_register_error = 1 # if sth went wrong show the error

        else: # if login form is popped up on site
            username = request.POST['jgu-username']
            password = request.POST['jgu-password']
            user = authenticate(request, username=username, password=password)
            if user is not None:    #if user authenticated successfully, log him in
                login(request, user)
                return redirect('home')
            show_login_error = 1 # if sth went wrong show the error

    else:  # else empy form
        form_register = UserRegisterForm()

    # get Errors and append them to array
    fehlermeldung_register = form_register.errors.as_data()
    fehlermeldung_register_str_arr = []
    for key in fehlermeldung_register:
        for error_arr in fehlermeldung_register[key]:
            fehlermeldung_register_str_arr += error_arr

    context = { # pass info variables to html
        'fehlermeldung_register_str_arr': fehlermeldung_register_str_arr,
        'show_register_error': show_register_error,
        'fehlermeldung_login': fehlermeldung_login,
        'show_login_error': show_login_error,
        'is_register': is_register,
    }
    return render(request, 'startsite/startseite.html', context)

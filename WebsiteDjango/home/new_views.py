from asyncore import file_dispatcher
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from utils import utils

@login_required
def home(request):
    # information to greet user correctly
    user = request.user
    first_name = '' if not user.first_name else user.first_name
    last_name = '' if not user.last_name else user.last_name
    use_username = True if not first_name and not last_name else False


    
    show_action = -1
    show_tasks = -1
    tasks = []

    if request.method == 'POST':
        action = 42 if not request.POST['jgu-action'] else request.POST['jgu-action']
        filter_applied = 0 if not request.POST['jgu-action-filter'] else request.POST['jgu-action-filter']


        if action == '0':
            # test exam

            show_action = 0
            pass
        elif action == '1' or filter_applied == 1:
            # exam
            if filter_applied:


            show_action = 1
            pass
        elif action == '2' or filter_applied == 1:
            # test sheet

            show_action = 2
            pass

    context = {
        'use_username'      : use_username,
        'first_name'        : first_name,
        'last_name'         : last_name,
        'username'          : user.username,

    }



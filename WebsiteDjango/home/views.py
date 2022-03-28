import imp
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .utils import utils
import random


# Create your views here.

@login_required
def home(request):
    user = request.user
    username = user.username
    first_name = ''
    last_name = ''
    use_username = True
    if user.first_name and user.last_name:
        use_username = False
        first_name = user.first_name
        last_name = user.last_name
    
    show_action = 3
    tasks = []
    subject = -1
    topic = -1
    difficulty = 0
    time = 0
    show_tasks = 0
    # all_subjects = utils.subjects()
    if request.method == 'POST':
        action = 9000
        if request.POST['jgu-action']:
            action = request.POST['jgu-action']
        
        if action == '0':
            # Probeklausur
            show_action = 0
        elif action == '1':
            # Klausur
            show_action = 1
            show_tasks = 1
        
        elif action == '2':
            show_action = 2
            show_tasks = 1

        elif action == '4' or action == '5':
            subject = request.POST['jgu-fachgebiet-filter']
            topic = request.POST['jgu-topic-filter']
            time = request.POST['jgu-time-filter']
            difficulty = request.POST['jgu-level-filter']
            filtered_tasks = utils.filter_aufgabe('Blubb', 2, 30)
            for task in filtered_tasks:
                tasks.append(task)
            if action == '4':
                show_action = 1
                show_tasks = 1
            else:
                show_action = 2
                show_tasks = 1
        elif action == '6':
            show_action = 2
            show_tasks = 1
            print('Test123')
            
        


    context = {
        'use_username'  : use_username,
        'username'      : username,
        'first_name'    : first_name,
        'last_name'     : last_name,
        'DOZENT'        : True,
        'tasks'         : tasks,
        'show_action'   : show_action,
        'show_tasks'    :show_tasks,
    }
    return render(request, 'home/index.html', context)

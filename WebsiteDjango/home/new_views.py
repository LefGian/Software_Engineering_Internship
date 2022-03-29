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
    subject = ''
    all_subjects = utils.get_fachgebiet()

    if request.method == 'POST':
        print(subject)
        action = 42 if not request.POST['jgu-action'] else request.POST['jgu-action']
        filter_applied = 0 if not request.POST['jgu-action-filter'] else request.POST['jgu-action-filter']
        subject = int(request.POST['jgu-fachgebiet-changed']) if subject != request.POST['jgu-fachgebiet-changed'] else ''
        topics_for_subject = utils.get_themengebiet(subject)

        if action == '0':
            # test exam

            show_action = 0
            pass
        elif action == '1' or filter_applied == 1:
            # exam
            if filter_applied:
                subject = request.POST['jgu-fachgebiet-filter']
                topic = request.POST['jgu-topic-filter']
                time = request.POST['jgu-time-filter']
                difficulty = request.POST['jgu-level-filter']
                filtered_tasks = utils.filter_aufgabe('Blubb', 2, 30)
                

            show_action = 1
            pass
        elif action == '2' or filter_applied == 1:
            # test sheet

            show_action = 2
            pass

    context = {
        'use_username'          : use_username,
        'first_name'            : first_name,
        'last_name'             : last_name,
        'username'              : user.username,
        'all_subjects'          : all_subjects,
        'topics_for_subject'    : topics_for_subject,
        'show_tasks'            : show_tasks,
        'show_action'           : show_action,
        'tasks'                 : tasks,
        'current_subject'       : subject,
        
    }
























from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from utils import utils



@login_required
def home(request):
    # greet user with real name or username if realnameis not known
    user = request.user
    print(user.groups.all())
    first_name = '' if not user.first_name else user.first_name
    last_name = '' if not user.last_name else user.last_name
    use_username = True if not first_name and not last_name else False

    show_action = 3
    show_tasks = 0
    tasks = []
    all_subjects = utils.get_fachgebiet()

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
            subject = request.POST['jgu-fachgebiet-filter']
            show_action = 2
            show_tasks = 1
            
        


    context = {
        'use_username'  : use_username,
        'username'      : user.username,
        'first_name'    : first_name,
        'last_name'     : last_name,
        'DOZENT'        : True,
        'tasks'         : tasks,
        'show_action'   : show_action,
        'show_tasks'    :show_tasks,
        'subjects'      : all_subjects,
    }
    return render(request, 'home/index.html', context)


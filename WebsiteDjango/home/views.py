from re import sub
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from utils import utils

@login_required
def home(request):
    # information to greet user correctly
    user = request.user
    user_group = utils.get_group(user)
    first_name = '' if not user.first_name else user.first_name
    last_name = '' if not user.last_name else user.last_name
    use_username = True if not first_name and not last_name else False


    time_list = [5, 10, 15, 20, 25, 30, 45, 60, 90, 120, 150, 180, 240, 300, 360]
    difficulty_list = ['Sehr leicht', 'Leicht', 'Mittel', 'Mäßig', 'Schwer', 'Sehr schwer', 'Hölle']
    selected_time = 0
    selected_difficulty = 0
    show_action = -1
    tasks = []
    task_list = []
    right_list = []
    test_list = []
    subject = None
    topic = None
    all_subjects = utils.get_fachgebiet()
    topics_for_subject = []

    if request.method == 'POST':
        action = request.POST['jgu-action']
        filter_applied = utils.check_if_value_is_set(request.POST['jgu-action-filter'])

        subject_id = utils.check_if_value_is_set(request.POST['jgu-fachgebiet-filter'])
        subject = utils.get_fachgebiet_by_id(subject_id)

        db_query_topics = utils.get_themengebiet(subject.id) if subject else []
        for topics in db_query_topics:
            topics_for_subject.append(topics)

        if action == '0':
            # test exam

            show_action = 0
            pass
        elif action == '1' or filter_applied == 1:
            # exam
           
            if filter_applied:
                topic_id = utils.check_if_value_is_set(request.POST['jgu-topic-filter'])
                topic = utils.get_themengebiet_by_id(topic_id)
                time = utils.check_if_value_is_set(request.POST['jgu-time-filter'])
                difficulty = utils.check_if_value_is_set(request.POST['jgu-level-filter'])
                tasks = utils.filter_aufgabe(topic_id, difficulty, time)

                selected_time = time
                selected_difficulty = difficulty
                

            show_action = 1
        elif action == '2' or filter_applied == 1:
            # test sheet

            show_action = 2
        if request.POST['jgu-task-list'] and request.POST['jgu-task-list'] != '[]':
            test_list = [ int(x) for x in request.POST['jgu-task-list'].split(',')]
            for task_id in test_list:
                right_list.append(utils.get_aufgabe_by_id(task_id))
            task_list = request.POST['jgu-task-list']
            

    context = {
        'use_username'          : use_username,
        'first_name'            : first_name,
        'last_name'             : last_name,
        'username'              : user.username,
        'user_group'            : user_group,

        'all_subjects'          : all_subjects,
        'current_subject'       : subject,
        'topics_for_subject'    : topics_for_subject,
        'current_topic'         : topic,

        'tasks'                 : tasks,
        'test_list'             : test_list,
        'task_list'             : task_list,
        'right_list'            : right_list,
        'show_action'           : show_action,
        'difficulty_list'       : difficulty_list,
        'selected_difficulty'   : selected_difficulty,
        'time_list'             : time_list,
        'selected_time'         : selected_time,
        
    }

    return render(request, 'home/index.html', context)


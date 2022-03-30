from ctypes import util
from re import sub
from django.http import HttpResponseRedirect
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

    tex_code = None

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
        filter_applied = utils.check_if_value_is_set(request.POST['jgu-action-filter']) if 'jgu-action-filter' in request.POST else 0

        subject_id = utils.check_if_value_is_set(request.POST['jgu-fachgebiet-filter']) if 'jgu-fachgebiet-filter' in request.POST else 0
        subject = utils.get_fachgebiet_by_id(subject_id) if subject_id != 0 else None

        db_query_topics = utils.get_themengebiet(subject.id) if subject else []
        for topics in db_query_topics:
            topics_for_subject.append(topics)

        if filter_applied:
            tasks, selected_time, selected_difficulty, topic = utils.apply_filter(request)
        if action == '0':
            # test exam
            show_action = 0
        elif action == '1':
            # exam
            show_action = 1
        elif action == '2':
            # test sheet
            show_action = 2
        if 'document-create' in request.POST and request.POST['document-create'] == '1':
            subject = utils.get_fachgebiet_by_id(request.POST['jgu-fachgebiet-filter'])
            topic = utils.get_themengebiet_by_id(request.POST['jgu-topic-filter'])
            difficulty = utils.check_if_value_is_set(request.POST['jgu-level-filter'])
            time = utils.check_if_value_is_set(request.POST['jgu-time-filter'])
            selected_tasks = []
            if utils.check_if_value_is_set(request.POST['random-tasks']):
                selected_tasks = utils.create_exam(topic.id, difficulty, time)
            else:
                selected_task_ids = [int(x) for x in request.POST['jgu-task-list'].split(',')]
                selected_tasks = [utils.get_aufgabe_by_id(task_id) for task_id in selected_task_ids]
            tex_code = utils.toLatex_html(selected_tasks, False)
            return redirect('questions')
        if 'jgu-task-list' in request.POST and request.POST['jgu-task-list'] != '[]' and request.POST['jgu-task-list']:
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


def questions(request):
    return render(request, 'home/questions.html', {})
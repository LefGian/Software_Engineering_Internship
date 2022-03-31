from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils import utils


@login_required
def home(request):
    """
    View that takes care of
        - creating a test exam
        - creating a normal exam
        - creating test sheets
        on the home page

    :param request: HttpRequest
    :type request: HttpRequest
    :return: render the home page
    :rtype: HttpResponse
    """    
    # variables to greet user accordingly to profil settings. If a user has entered his first and last name he will be greeted with these. Else he will be greeted with hhis username
    user = request.user
    user_group = utils.get_group(user)
    first_name = '' if not user.first_name else user.first_name
    last_name = '' if not user.last_name else user.last_name
    use_username = True if not first_name and not last_name else False
    context = {}
    tex_code = None

    time_list = [5, 10, 15, 20, 25, 30, 45, 60, 90, 120, 150, 180, 240, 300, 360]
    difficulty_list = ['Sehr leicht', 'Leicht', 'Mittel', 'Mäßig', 'Schwer', 'Sehr schwer', 'Hölle']

    # keeps track of last selected time and difficulty
    selected_time = 0
    selected_difficulty = 0

    action = None                           # keep track of the action that needs to be loaded (test exam, exam or test sheet)
    tasks = []                              # list of tasks according to applied filter
    selected_tasks = ''                     # list of tasks selected by the user in string format to pass it back to the html via context
    selected_tasks_as_list = []             # list of tasks selected by the user as a list of int for deciding if tasks for filtering in left side and right side of selection 
    subject = None                          
    topic = None                            
    all_subjects = utils.get_fachgebiet()   
    topics_for_subject = []                 # list of topics for according subject

    if request.method == 'POST':
        # action shows which action is selected (test exam, exam, test sheet)
        action = utils.check_if_value_is_set(request.POST['jgu-action'])
        filter_applied = utils.check_if_value_is_set(
            request.POST['jgu-action-filter']) if 'jgu-action-filter' in request.POST else 0

        # get selected subject and the right topics
        subject_id = utils.check_if_value_is_set(
            request.POST['jgu-fachgebiet-filter']) if 'jgu-fachgebiet-filter' in request.POST else 0
        subject = utils.get_fachgebiet_by_id(subject_id) if subject_id != 0 else None
        db_query_topics = utils.get_themengebiet(subject_id) if subject else []
        for topics in db_query_topics:
            topics_for_subject.append(topics)

        # get selection of tasks according to filter atributes
        if filter_applied:
            tasks, selected_time, selected_difficulty, topic = utils.apply_filter(request)

        # get the list of tasks selected by user when creating exams or test sheets
        if 'jgu-task-list' in request.POST \
            and request.POST['jgu-task-list']:
            selected_tasks_as_list = [int(x) for x in request.POST['jgu-task-list'].split(',')]
            for task_id in selected_tasks_as_list:
                tasks.append(utils.get_aufgabe_by_id(task_id))
            selected_tasks = request.POST['jgu-task-list']
        
        # document creation part
        if utils.check_if_value_is_set(request.POST['document-create']):
            if 'create-test-exam' in request.POST:
                # get tasks that fit in the selceted time and difficulty
                topic, difficulty, time = utils.get_filter_attributes(request)
                selected_tasks = utils.create_exam(topic, difficulty, time)
            else:
                # get tasks that are selected by user
                selected_task_ids = [int(x) for x in request.POST['jgu-task-list'].split(',')]
                selected_tasks = [utils.get_aufgabe_by_id(task_id) for task_id in selected_task_ids]

            show_results = False
            if 'jgu-show-results' in request.POST:
                show_results = True
            
            # creates the LaTeX code that can then be copied or downloaded
            tex_code = utils.toLatex(selected_tasks, show_results)
            data_str = utils.file_to_str(tex_code.name)

            # redirect to page where LaTeX code can be copied or downloaded
            return render(request, 'downloadapp/download.html', {'tex_code': data_str, })

    context = {
        'use_username': use_username,
        'first_name': first_name,
        'last_name': last_name,
        'username': user.username,
        'user_group': user_group,

        'all_subjects': all_subjects,
        'selected_subject': subject,
        'topics_for_subject': topics_for_subject,
        'selected_topic': topic,

        'tasks': tasks,
        'selected_tasks_as_list': selected_tasks_as_list,
        'selected_tasks': selected_tasks,

        'action': action,

        'difficulty_list': difficulty_list,
        'selected_difficulty': selected_difficulty,
        'time_list': time_list,
        'selected_time': selected_time,
    }

    return render(request, 'home/index.html', context)

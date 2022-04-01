from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from utils import utils


@login_required
def createassignment(request):
    """Django-View that is used to call aufgabeerstellen.html site

    :param request: HttpRequest request from Django, that delivers all the Information
    :type request: HttpRequest
    :return: render of createassignment/aufgabeerstellen.html with context Dict
    :rtype: HttpResponse
    """    
    error_messages = [] # Array holding the error messages, later displayed in html
    show_error = 0  # shows if error_messages should be displayed
    user = request.user
    all_subjects = utils.get_fachgebiet()
    # if the user is not of group 'Dozent' -> redirect
    if not ('Dozent' in utils.get_group(user=user)):
       return redirect('userprofile-userprofile')
    jgu_save = 0
    chose_fachgebiet = 0

    task_name = ''


    time_list = [5, 10, 15, 20, 25, 30, 45, 60, 90, 120, 150, 180, 240, 300, 360]   # times available to choose from in Bearbeitungszeit
    difficulty_list = ['Sehr leicht', 'Leicht', 'Mittel', 'Mäßig', 'Schwer', 'Sehr schwer', 'Hölle']    # difficulties available to choose from
    all_subjects = utils.get_fachgebiet()   # get subjects from DB
    topics_for_subject = []
    cur_subject = None

    if request.method == 'POST':
        jgu_save = request.POST['jgu-save']
        aufgabe_dict = {    # Dict with all the info we get from our Form when submitted
            'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'name': request.POST['jgu-task-name'],
            'aufgabenstellung': request.POST['jgu-task-code'],
            'loesung': request.POST['jgu-task-result'],
            'user': user,
            'schwierigkeit': request.POST['jgu-level'],
            'zeit': request.POST['jgu-time'],
            'themengebiet': request.POST['jgu-topic'],
            'fachgebiet': request.POST['jgu-fachgebiet'],
            'chose_fachgebiet': request.POST['chose_fachgebiet'],
        }
        # get info from DB
        subject_id = utils.check_if_value_is_set(request.POST['jgu-fachgebiet'])
        cur_subject = utils.get_fachgebiet_by_id(subject_id)
        topics = utils.get_themengebiet(subject_id) if cur_subject else []
        topics_for_subject = [topic for topic in topics]

        if aufgabe_dict['chose_fachgebiet'] == '0':
            # try to safe Aufgabe in DB, show_error = 0 if went well -1 otherwise
            show_error = utils.add_aufgabe(aufgabe_dict['name'],
                                           aufgabe_dict['aufgabenstellung'],
                                           aufgabe_dict['loesung'],
                                           user, aufgabe_dict['schwierigkeit'],
                                           aufgabe_dict['zeit'],
                                           aufgabe_dict['themengebiet'])
        
        if(show_error == -1): show_error = 1    # set to 1 if we have error
        if(show_error): # add error message 
            error_messages = ['Input Error. Check your input']
        chose_fachgebiet = request.POST['chose_fachgebiet']
        if 'jgu-task-name' in request.POST: task_name = request.POST['jgu-task-name']

    context = { # pass info variables to html
        'error_messages': error_messages,
        'show_error': show_error,
        'all_subjects': all_subjects,
        'topics_for_subject': topics_for_subject,
        'cur_subject': cur_subject,
        'time_list': time_list,
        'difficulty_list': difficulty_list,
        'jgu_save': int(jgu_save),
        'chose_fachgebiet': int(chose_fachgebiet),
        'task_name' : task_name,

    }
    return render(request, 'createassignment/aufgabeerstellen.html', context)

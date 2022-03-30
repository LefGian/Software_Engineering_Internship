#from cv2 import log
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import AufgabeErstellenForm
from utils import utils


# Create your views here.

@login_required
def createassignment(request):
    error_messages = ['Input Error. Check your input']
    show_error = 0
    user = request.user
    if not ('Dozent' in utils.get_group(user=user)):
       return redirect('userprofile-userprofile')
    


    time_list = [5, 10, 15, 20, 25, 30, 45, 60, 90, 120, 150, 180, 240, 300, 360]
    difficulty_list = ['Sehr leicht', 'Leicht', 'Mittel', 'Mäßig', 'Schwer', 'Sehr schwer', 'Hölle']
    all_subjects = utils.get_fachgebiet()
    topics_for_subject = []
    cur_subject = None

    aufgabe_erstellen_form = AufgabeErstellenForm(instance=user)


    if request.method == 'POST':
        aufgabe_dict = {
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


        subject_id = utils.check_if_value_is_set(request.POST['jgu-fachgebiet'])
        cur_subject = utils.get_fachgebiet_by_id(subject_id)
        topics = utils.get_themengebiet(subject_id) if cur_subject else []
        topics_for_subject = [topic for topic in topics]
        print(aufgabe_dict['chose_fachgebiet'])

        if(aufgabe_dict['chose_fachgebiet'] == '0'):
            show_error = utils.add_aufgabe(aufgabe_dict['name'], aufgabe_dict['aufgabenstellung'],
                                    aufgabe_dict['loesung'], user, aufgabe_dict['schwierigkeit'],
                                    aufgabe_dict['zeit'], aufgabe_dict['themengebiet'])
        

    context = {
        'error_messages': error_messages,
        'show_error': show_error,
        'all_subjects': all_subjects,
        'topics_for_subject': topics_for_subject,
        'cur_subject': cur_subject,
        'time_list': time_list,
        'difficulty_list': difficulty_list,

    }
    return render(request, 'createassignment/aufgabeerstellen.html', context)

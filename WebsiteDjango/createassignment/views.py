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
        }


        show_error = utils.add_aufgabe(aufgabe_dict['name'], aufgabe_dict['aufgabenstellung'],
                                aufgabe_dict['loesung'], user, aufgabe_dict['schwierigkeit'],
                                aufgabe_dict['zeit'], aufgabe_dict['themengebiet'], fachgebiet = int(aufgabe_dict['fachgebiet']))
        

    context = {
        'error_messages': error_messages,
        'show_error': show_error
    }
    return render(request, 'createassignment/aufgabeerstellen.html', context)

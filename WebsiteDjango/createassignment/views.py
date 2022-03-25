from tokenize import group
from cv2 import log
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash
from .forms import AufgabeErstellenForm
from django.contrib.auth.decorators import user_passes_test
from utils import utils
from django.contrib.auth.models import User


# Create your views here.

@login_required
def createassignment(request):
    user = request.user
    if not ('Dozent' in utils.get_group(user=user)):
       return redirect('userprofile-userprofile')
    
    aufgabe_erstellen_form = AufgabeErstellenForm(instance=user)


    if request.method == 'POST':
        aufgabe_dict = {
            'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'name': request.POST['jgu-task-name'],
            'aufgabenstellung': request.POST['jgu-task-code'], # richtiger name ?
            'loesung': request.POST['jgu-task-result'], # richtiger name ?
            'user': user,
            'schwierigkeit': request.POST['jgu-level'],
            'zeit': request.POST['jgu-time'],
            'themengebiet': request.POST['jgu-topic'],
        }

        # falls eingaben richtig:
            #in datenbank speichern

    context = {
        'testvar': 12
    }
    return render(request, 'createassignment/aufgabeerstellen.html', context)
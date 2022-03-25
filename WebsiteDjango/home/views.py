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
    

    subjects = []
    if request.method == 'POST':
        if request.POST['jgu-action'] == 0:
            # Probeklausur
            pass
        elif request.POST['jgu-action'] == 1:
            # Klausur
            subject = request.POST['jgu-fachgebiet-filter']
            topic = request.POST['jgu-topic-filter']
            time = request.POST['jgu-time-filter']
            difficulty = request.POST['jgu-level-filter']
            tasks = utils.filter_aufgabe(topic, difficulty, time)

        utils.add_aufgabe('Test', 'a+b+c', 'd', user, 2, 30,
                'Blubb')





    context = {
        'use_username'  : use_username,
        'username'      : username,
        'first_name'    : first_name,
        'last_name'     : last_name,
        'DOZENT' : True,
    }
    return render(request, 'home/index.html', context)



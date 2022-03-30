from django.shortcuts import render

# Create your views here.

def download(request):

    context = {
        'testvar': 1,
    }
    return render(request, 'downloadapp/download.html', context)
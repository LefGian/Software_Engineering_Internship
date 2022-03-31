from django.shortcuts import render


def download(request):
    context = {
        'testvar': 1,
    }
    return render(request, 'downloadapp/download.html', context)

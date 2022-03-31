from django.shortcuts import render


def download(request):
    """
    this view is only here for competion purposes, it is normally not used but can later be used

    :param request: HttpRequest request from Django
    :type request: HttpRequest
    :return: render of downloadapp/download.html with context Dict
    :rtype: HttpResponse
    """    
    context = {
        'testvar': 1,
    }
    return render(request, 'downloadapp/download.html', context)

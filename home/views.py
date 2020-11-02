from django.shortcuts import render

# Views


def index(request):
    """ Renders the Index page """

    return render(request, 'home/index.html')

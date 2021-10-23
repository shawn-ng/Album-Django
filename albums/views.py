from django.http.response import HttpResponse
from django.shortcuts import render


from .models import Albums

# Create your views here.


def index(request):

    # grabbing what we need from data base
    list = Albums.objects
    # creating a context
    context = {"albums": list}
    # we are rendering on a template
    return render(request, '/index.html', context)

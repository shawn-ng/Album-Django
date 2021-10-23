from django.http.response import HttpResponse
from django.shortcuts import render


from .models import Albums

# Create your views here.


def index(request):

    # grabbing what we need from data base
    list = Albums.objects.all()
    # creating a context
    context = {"albums": list}
    # we are rendering on a template
    return render(request, 'albums/index.html', context)


def albums(request):
    if request.method == "GET":
        return read(request)
    if request.method == "POST":
        return create(request)


def album(request):
    if request.method == "GET":
        return read_one(request)
    if request.method == "PATCH":
        return update(request)
    if request.method == "DELETE":
        return delete(request)


def create(request):

    return HttpResponse("Create")


def read(request):

    return HttpResponse("Read")


def read_one(request):

    return HttpResponse("Read One")


def update(request):

    return HttpResponse("Update")


def delete(request):

    return HttpResponse("delete")

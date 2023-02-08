from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return HttpResponse("Hello Nour")

# Create your views here.

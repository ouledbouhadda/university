from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hiiiii")

# Create your views here.

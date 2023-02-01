from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello this Rahma")

# Create your views here.

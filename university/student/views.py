from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
     template = loader.get_template('index.html')
     context = { 'n' :{'note1': 23,'note2':24,'note3':20,'note4':12}}
     return HttpResponse(template.render(context, request))
# Create your views here.
def emploi(request):
    return HttpResponse('emploi')
def test(request):
     return render(request,'class.html')
    
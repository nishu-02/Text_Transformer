from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def rempunc(request):
    return HttpResponse("Remove punctuutaion")

def cap(request):
    return HttpResponse("Captilize the entire input")

def newlineremove(request):
    return HttpResponse("Captilize the entire input")

def spacerem(request):
    return HttpResponse("Captilize the entire input")

def charcount(request):
    return HttpResponse("Captilize the entire input")
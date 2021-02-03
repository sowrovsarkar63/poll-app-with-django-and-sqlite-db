from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("this is working from polls app ")
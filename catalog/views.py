from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Yo Hello everyone! This is my book catalog.")

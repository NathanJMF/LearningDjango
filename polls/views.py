from django.shortcuts import render
from django.http import HttpResponse


# Created index view part of the polls app.
def index(request):
    return HttpResponse("Hello!")


# Created a test view also part of the polls app.
def test(request):
    return HttpResponse("This is a test!")

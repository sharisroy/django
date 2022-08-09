from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return HttpResponse("This is Employee home page")


def about(request):
    data = "This is our Employee page, this message comes from data variable"
    return HttpResponse(data)


def contact(request):
    return HttpResponse('This is Employee contact page')


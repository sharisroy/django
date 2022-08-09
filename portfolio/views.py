from django.http import HttpResponse


def home(request):
    return HttpResponse("This is our home page")


def about(request):
    data = "This is our about page, this message comes from data variable"
    return HttpResponse(data)


def contact(request):
    return HttpResponse('This is our contact page')

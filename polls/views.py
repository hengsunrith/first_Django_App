from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")


def contact(request):
    return HttpResponse("<h1>Contact Us</h1>")
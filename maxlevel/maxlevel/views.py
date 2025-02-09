from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi there, This is my first django web")

def about(request):
    return HttpResponse("Hi there, This is my first django web")

def contact(request):
        return HttpResponse("Hi there, This is my first django web")
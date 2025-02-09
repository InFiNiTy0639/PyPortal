from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    # return HttpResponse("Hi there, This is my first django web")
    return render(req,'index.html')

def about(request):
    return HttpResponse("Hi there, This is my first django web")

def contact(request):
        return HttpResponse("Hi there, This is my first django web")
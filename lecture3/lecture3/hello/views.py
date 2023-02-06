from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def goku(request):
    return HttpResponse("Hello Goku")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def name(request, name):
    return render(request, "hello/name.html", {
        "name": name.capitalize()
    })
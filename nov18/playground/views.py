from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello-world")

def say_hello(request):
    return render(request, 'index.html')



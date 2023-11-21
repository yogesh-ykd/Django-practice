from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def mynews(request):
    return render(request, 'home.html')
from django.shortcuts import render
from django.http import HttpResponse

def port(request):
    return render(request, 'index.html')


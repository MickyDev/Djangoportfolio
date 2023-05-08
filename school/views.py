from django.shortcuts import render
from django.http import HttpResponse

def myschool(request):
    return HttpResponse('This is my school!!!')
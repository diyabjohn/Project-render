from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Hey it's me Diya Biji John . Welcome to My Django Project - Project Render!")


# Create your views here.

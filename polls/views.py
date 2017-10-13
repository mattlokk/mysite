"""polls app"""

# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """ index """    
    return HttpResponse("Hey there duder")

# Create your views here.
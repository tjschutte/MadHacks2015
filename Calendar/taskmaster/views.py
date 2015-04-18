from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.

def index(request):
    return HttpResponse("Hello, you are now on the test site<br>Andrew")

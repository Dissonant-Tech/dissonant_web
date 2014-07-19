from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    t = loader.get_template('index.html')
    c = Context({"page": "Home"})
    return HttpResponse(t.render(c));

def projects(request):
    t = loader.get_template('projects.html')
    c = Context({"page": "Projects"})
    return HttpResponse(t.render(c));

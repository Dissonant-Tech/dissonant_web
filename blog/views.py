from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader

from blog.models import Category

def index(request):
    t = loader.get_template('index.html')
    c = Context({"page": "Home"})
    return HttpResponse(t.render(c));

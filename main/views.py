from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader

from blog.models import Category, Article

def index(request):
    t = loader.get_template('index.html')
    articles = Article.objects.all().filter(published=True)
    c = Context({"page": "Home", "articles": articles})

    return HttpResponse(t.render(c))

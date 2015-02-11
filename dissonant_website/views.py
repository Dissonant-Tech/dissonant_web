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

def projects(request):
    t = loader.get_template('projects.html')
    c = Context({"page": "Projects"})

    return HttpResponse(t.render(c))

def tags(request):
    t = loader.get_template('tags.html')
    articles = Article.objects.all().filter(published=True)
    tag_dict = {}
    for article in articles:
        for tag in article.categories.all():
            if tag.title not in tag_dict.keys():
                tag_dict[tag.title] = []
                tag_dict[tag.title].append(article)
            else:
                tag_dict[tag.title].append(article)

    c = Context({"page": "Tags", "tag_dict": tag_dict})

    return HttpResponse(t.render(c))

def contact(request):
    t = loader.get_template('contact.html')
    c = Context({"page": "Contact"})

    return HttpResponse(t.render(c))

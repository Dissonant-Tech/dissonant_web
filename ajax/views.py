from django.http import HttpResponse, Http404
from blog.models import Category, Article
import json

def index(request):
    """Ajax call"""
    articles = Article.objects.all()
    results = [obj.as_json() for obj in articles]
    return HttpResponse(json.dumps(results), content_type='application/json')

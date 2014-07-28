from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
import calendar, datetime

def index(request):
    """Blog index"""
    archive_dates = Article.objects.dates('date_publish', 'month', order='DESC')
    categories = Category.objects.all()

    page = request.GET.get('page')
    article_queryset = Article.objects.all()
    paginator = Paginator(article_queryset, 5)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render(
            request,
            "blog/article/index.html",
            {
                "articles": articles,
                "archive_dates": archive_dates,
                "categories": categories,
            }
        )

def single(request, slug):
    """A Single Article"""
    article = get_object_or_404(Article, slug=slug)
    archive_dates = Article.objects.dates('date_publish', 'month', order='DESC')
    categories = Category.objects.all()

    return render(
            request,
            'blog/article/single.html',
            {
                "article": article,
                "archive_dates": archive_dates,
                "categories": categories,
            }
        )

def date_archive(request, year, month):
    """Blog Date Archive"""
    year = int(year)
    month = int(month)
    month_range = calendar.monthrange(year, month)
    start = datetime.datetime(year=year, month=month, day=1)
    end = datetime.datetime(year=year, month=month, day=month_range[1])

    archive_dates = Article.objects.dates('date_publish', 'month', order='DESC')
    categories = Category.objects.all()

    # Pagination
    page = request.GET.get('page')
    article_queryset = Article.objects.filter(date_publish__range=(start.date(), end.date()))
    paginator = Paginator(article_queryset, 5)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render(
            request,
            "blog/article/date_archive.html",
            {
                "start": start,
                "end": end,
                "articles": articles,
                "archive_dates": archive_dates,
                "categories": categories,
            }
        )

def category_archive(request, slug):
    archive_dates = Article.objects.dates('date_publish', 'month', order='DESC')
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)

    # Pagination
    page = request.GET.get('page')
    article_queryset = Article.objects.filter(categories = category)
    category = get_object_or_404(Category, slug=slug)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render(
            request,
            "blog/article/date_archive.html",
            {
                "articles": articles,
                "archive_dates": archive_dates,
                "categories": categories,
                "category" : category
            }
        )

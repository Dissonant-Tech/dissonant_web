from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url('^blog/archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'blog.views.article.date_archive', name="blog-date-archive"),
    url('^blog/archive/(?P<slug>[-\w]+)/$', 'blog.views.article.category_archive', name="blog-category-archive"),
    url('^blog/(?P<slug>[-\w]+)/$', 'blog.views.article.single', name="blog-article-single"),
    url('^blog/$', 'blog.views.article.index', name="blog-article-index"),
)

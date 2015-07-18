from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'blog.views.date_archive', name="blog-date-archive"),
    url(r'^archive/(?P<slug>[-\w]+)/$', 'blog.views.category_archive', name="blog-category-archive"),
    url(r'^(?P<slug>[-\w]+)/$', 'blog.views.single', name="blog-article-single"),
)

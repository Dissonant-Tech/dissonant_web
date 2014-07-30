from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url('^archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'blog.views.date_archive', name="blog-date-archive"),
    url('^archive/(?P<slug>[-\w]+)/$', 'blog.views.category_archive', name="blog-category-archive"),
    url('^(?P<slug>[-\w]+)/$', 'blog.views.single', name="blog-article-single"),
    url('^/ajax/$', 'blog.views.ajax', name="blog-ajax"),
    url('^$', 'blog.views.index', name="blog-article-index"),
)

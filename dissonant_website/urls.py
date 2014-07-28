from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from main import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^blog/archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'blog.views.article.date_archive', name="blog-date-archive"),
    url('^blog/archive/(?P<slug>[-\w]+)/$', 'blog.views.article.category_archive', name="blog-category-archive"),
    url('^blog/(?P<slug>[-\w]+)/$', 'blog.views.article.single', name="blog-article-single"),
    url('^blog/$', 'blog.views.article.index', name="blog-article-index"),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.COMPONENT_URL, document_root=settings.COMPONENT_ROOT)

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from dissonant_website import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^projects/$', views.projects, name='projects'),
                       url(r'^tags/$', views.tags, name='tags'),
                       url(r'^contact/$', views.contact, name='contact'),
                       url(r'^blog/$', views.index, name='index'),
                       url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

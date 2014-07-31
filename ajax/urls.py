from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'ajax.views.index', name="ajax-index"),
)

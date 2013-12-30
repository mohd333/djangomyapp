from django.conf.urls import patterns, include, url
from firstproject.views import hello
from firstproject.views import current_time, hours_ahead
from books.views import search_form, search


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello),
    url(r'^time/$', current_time),
    url(r'^time/plus/(\d+)/$', hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search-form/$', search_form),
    (r'^search/$', search)
    )

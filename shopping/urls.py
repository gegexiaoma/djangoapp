from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopping.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'shop.views.index', name='home'),
    url(r'^user$', 'shop.views.user', name='users'),
    url(r'^book$', 'shop.views.book', name='books'),
    url(r'^admin/', include(admin.site.urls)),
)

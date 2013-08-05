from django.conf.urls import patterns, include, url
#from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
#    url(r'^inscricao/(\d+)/$', 'eventex.subscriptions.views.detail', name='detail'),
    # url(r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('eventex.core.urls', namespace='core')),
)
#urlpatterns += patterns('',
#        url(r'^static/(?P<path>.*)$', 'serve', {'document_root': settings.STATIC_ROOT}),)

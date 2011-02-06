from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^karma/', include('karma.foo.urls')),

    (r'^$', 'karma.views.index'), 
    (r'^login/$', 'karma.views.login'), 
    (r'^logout/$', 'karma.views.logout'), 
    (r'^users/$', 'karma.views.userindex'), 
    (r'^users/(?P<user_id>\d+)/$', 'karma.views.userkarma'), 
    (r'^points/', include('karma.points.urls')), 
    (r'^api/', include('karma.api.urls')), 

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        # url(r'^favicon\.ico$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'path': 'favicon.ico'}),
        # url(r'^404/$', direct_to_template, {'template': '404.html'}),
        # url(r'^500/$', direct_to_template, {'template': '500.html'}),
    )

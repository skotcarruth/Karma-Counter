from django.conf.urls.defaults import *

urlpatterns = patterns('karma.api.views',
    (r'^users/$', 'users'), 
    (r'^users/(?P<user_id>\d+)/$', 'userkarma'), 
    (r'^users/(?P<user_id>\d+)/(?P<value>(up|down))$', 'add'), 
)

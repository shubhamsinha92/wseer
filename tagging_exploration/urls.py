from django.conf.urls.defaults import *
from django.contrib.auth.views import password_reset, password_reset_done, password_change, password_change_done
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
  (r'^admin/', include('django.contrib.admin.urls')),
  (r'^accounts/', include('registration.urls')),
)

urlpatterns += patterns('',
  (r'^accounts/profile/$', direct_to_template, {'template': 'registration/profile.html'}),
  (r'^accounts/password_reset/$', password_reset, {'template_name': 'registration/password_reset.html'}),
  (r'^accounts/password_reset_done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}),
  (r'^accounts/password_change/$', password_change, {'template_name': 'registration/password_change.html'}),
  (r'^accounts/password_change_done/$', password_change_done, {'template_name': 'registration/password_change_done.html'}),
)

from django.contrib.restful_model_views.restful_urls import get_restful_patterns
urlpatterns += get_restful_patterns()


   

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<feature_request_id>[0-9]+)/$', views.editDescription, name='detail'),
    url(r'^edit_description/(?P<feature_request_id>[0-9]+)/$', views.editDescription, name='edit_description'),
    url(r'^edit/(?P<feature_request_id>[0-9]+)/$', views.edit, name='edit_request'),
    url(r'^delete/(?P<feature_request_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^new/$', views.new, name='new'),
    url(r'^test/$', views.addTestData, name='test'),
    url(r'^login/$', 'feature_requests.auth_views.login_view'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/feature_requests/login'}),
    url(r'^auth/$', 'feature_requests.auth_views.auth_and_login'),
    url(r'^signup/$', 'feature_requests.auth_views.sign_up_in'),

]

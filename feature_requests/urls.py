from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^detail/(?P<feature_request_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^delete/(?P<feature_request_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^new/$', views.new, name='new'),
    url(r'^test/$', views.addTestData, name='test')
    # ex: /feature_request_id/5/results/
#url(r'^$', views.results, name='results'),

]

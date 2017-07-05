from django.conf.urls import  url
from howdy import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
        url(r'^(?P<website_id>[0-9]+)/$', views.detail,name='detail'),
]

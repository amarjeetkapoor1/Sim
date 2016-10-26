from django.conf.urls import url

from . import views

urlpatterns = [
    #directs to index veiw

    url(r'^index/$', views.index, name='index'),
    url(r'^getfile/$', views.getfile, name='getfile'),
    url(r'^index/(?P<name>\w+)/$',views.tables),
    url(r'^output/$', views.output, name = 'output'),
    url(r'^table/$', views.table, name = 'table')
]

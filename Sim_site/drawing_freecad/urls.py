from django.conf.urls import url

from . import views

urlpatterns = [
    #directs to index veiw
    url(r'^drawing/$', views.index, name='index'),
    url(r'^drawing/specs/$', views.specs, name='specs'),
    url(r'^drawing/download/$', views.download, name='download'),
    url(r'^drawing/drawing/$', views.drawing, name='drawing')
]

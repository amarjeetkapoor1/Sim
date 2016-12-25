#***********************************************************************
#*                                                                     *
#*   File:                                                             *
#*       urls.py                                                       *
#*                                                                     *
#*   Author:                                                           *
#*      Amritpal Singh <amrit3701@gmail.com>                           *
#*                                                                     *
#*   Brief:                                                            *
#*      This program file require for Django.                          *
#*                                                                     *
#***********************************************************************

from django.conf.urls import url

from . import views

from django.views.generic import TemplateView

urlpatterns = [
    #directs to index veiw
    url(r'^drawing/$', views.index, name='index'),
    url(r'^drawing/specs/$', views.specs, name='specs'),
    url(r'^drawing/download/$', views.download, name='download'),
    url(r'^drawing/drawing/$', views.drawing, name='drawing'),
    #url(r'^drawing/show/$', TemplateView.as_view(template_name='drawing_freecad/show.html'), name='convert_fcstd2webgl')
    url(r'^drawing/show/$', views.convert_fcstd2webgl, name='convert_fcstd2webgl')
]

from django.conf.urls import url, include, patterns
from classes import views

urlpatterns = [
    url(r'^$', views.ClassesList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ClassesDetail.as_view()),
    url(r'^(?P<pk>[0-9]+)/semester/$', views.SemesterList.as_view()),
]

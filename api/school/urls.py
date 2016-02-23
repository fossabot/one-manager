from django.conf.urls import url, include, patterns
from school import views

urlpatterns = [
    url(r'^$', views.SchoolList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.SchoolDetail.as_view()),
]

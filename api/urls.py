from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/swagger/', include('rest_framework_swagger.urls')),
    url(r'^docs/drf/', include('rest_framework_docs.urls')),
    url(r'^api/', include('accounts.urls')),
    url(r'^api/', include('school.urls')),
    url(r'^api/', include('classes.urls')),
]

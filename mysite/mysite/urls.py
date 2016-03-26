from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
url(r'^polls/', include('polls.urls')),
url(r'^admin/', admin.site.urls),
    ]

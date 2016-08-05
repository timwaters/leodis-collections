"""leodis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  fromfrom django.conf import settings other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gallery.views.index'), 
    #url(r'^collection/(?P<collection_id>[0-9]+)/photo/(?P<photo_id>[0-9]+)$', 'gallery.views.photo', name='photo'),
    url(r'^photo/(?P<photo_id>[0-9]+)$', 'gallery.views.photo', name='photo'),
    url(r'^collection/(?P<collection_id>[0-9]+)$', 'gallery.views.collection', name='collection'),
    url(r'^collection/(?P<collection_id>[0-9]+).geojson$', 'gallery.views.collection_geojson', name='collection_geojson'),
    url(r'^about', 'gallery.views.about'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

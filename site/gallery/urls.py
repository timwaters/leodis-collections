from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^collection/(?P<collection_id>.+)$', 'gallery.views.collection', name='collection'),
]
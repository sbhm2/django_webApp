from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    url(r'^api/list$', views.list),
]

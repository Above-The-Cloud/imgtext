
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

from articles import views

urlpatterns = [
    re_path(r'^hello$', views.hello),
]
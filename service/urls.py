from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

from service import views


urlpatterns = [
    re_path(r'^articles/', include('articles.urls')),
]
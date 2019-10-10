from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

from imgtext import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^hello$', views.hello),
    re_path(r'^static/(?P<path>.*)$',serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^service/', include('service.urls')),
]
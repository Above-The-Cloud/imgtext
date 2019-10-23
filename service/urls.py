from django.urls import path, re_path, include


urlpatterns = [
    re_path(r'^articles/', include('articles.urls')),
    re_path(r'^category/', include('category.urls')),
]
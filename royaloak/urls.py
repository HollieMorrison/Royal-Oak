from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Admin panel
    path("admin/", admin.site.urls),
    # Main app routes
    path("", include("myapp.urls")),  # links to myapp/urls.py
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication & Family Member APIs
    path("api/auth/", include("apps.users.urls")),

    # Document APIs
    path("api/", include("apps.documents.urls")),
]
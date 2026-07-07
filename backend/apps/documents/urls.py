from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DocumentViewSet

router = DefaultRouter()
router.register("documents", DocumentViewSet, basename="document")
  # router = DefaultRouter(): ---------Think of the router as an automatic URL generator.-
  # Instead of manually writing:
  #path("documents/", ...)
  #path("documents/<int:pk>/", ...)
  #path("documents/create/", ...)
  #the router generates them for you.

urlpatterns = [
    path("", include(router.urls)),
]
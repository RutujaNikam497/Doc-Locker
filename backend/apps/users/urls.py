print("LOADED apps.users.urls")
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import FamilyMemberViewSet

router = DefaultRouter()
router.register("family-members", FamilyMemberViewSet, basename="family-member")

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]

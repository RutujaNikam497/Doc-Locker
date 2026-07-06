# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import FamilyMember
from .serializers import FamilyMemberSerializer


class FamilyMemberViewSet(viewsets.ModelViewSet):
    serializer_class = FamilyMemberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FamilyMember.objects.filter(owner=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
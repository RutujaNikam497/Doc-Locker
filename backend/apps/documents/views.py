from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    # Meaning:
    #Only logged-in users with a valid JWT token can access these APIs.
    #If someone sends a request without a token:
    #401 Unauthorized

    def get_queryset(self):
        return Document.objects.filter(owner=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
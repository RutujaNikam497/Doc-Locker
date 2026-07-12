from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    # Add this
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Document.objects.filter(
            owner=self.request.user
        ).order_by("-created_at")

    def perform_create(self, serializer):
        print("FILES:", self.request.FILES)
        print("DATA:", self.request.data)
        serializer.save(owner=self.request.user)
        
from datetime import date

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.documents.models import Document
from apps.users.models import FamilyMember

from .serializers import (
    UpcomingDocumentSerializer,
    MonthlyActionSerializer,
)
class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

     documents = Document.objects.filter(owner=request.user)
     family_members = FamilyMember.objects.filter(owner=request.user)

     valid = 0
     expiring = 0
     action_required = 0
     no_expiry = 0

     for document in documents:

        status = document.get_status()

        if status == "VALID":
            valid += 1

        elif status == "EXPIRING":
            expiring += 1

        elif status == "ACTION_REQUIRED":
            action_required += 1

        elif status == "NO_EXPIRY":
            no_expiry += 1

     return Response({
        "total_documents": documents.count(),
        "family_members": family_members.count(),
        "valid": valid,
        "expiring": expiring,
        "action_required": action_required,
        "no_expiry": no_expiry,
     })

class UpcomingExpiryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        documents = Document.objects.filter(
            owner=request.user,
            expiry_date__isnull=False
        ).order_by("expiry_date")

        upcoming = []
        today = date.today()

        for document in documents:

            if document.get_status() == "EXPIRING":

                upcoming.append({
                    "title": document.title,
                    "family_member": document.family_member.full_name,
                    "document_type": document.document_type,
                    "expiry_date": document.expiry_date,
                    "status": document.get_status(),
                    "days_left": (document.expiry_date - today).days,
                })

        serializer = UpcomingDocumentSerializer(upcoming, many=True)
        return Response(serializer.data)   

class MonthlyActionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        documents = Document.objects.filter(
            owner=request.user,
            expiry_date__isnull=False
        ).order_by("expiry_date")

        actions = []

        today = date.today()

        for document in documents:

            status = document.get_status()

            if status in ["EXPIRING", "ACTION_REQUIRED"]:

                actions.append({
                    "title": document.title,
                    "family_member": document.family_member.full_name,
                    "document_type": document.document_type,
                    "action": f"Renew {document.get_document_type_display()}",
                    "days_left": (document.expiry_date - today).days,
                })

        serializer = MonthlyActionSerializer(actions, many=True)

        return Response(serializer.data)
    
class MonthlyActionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        documents = Document.objects.filter(
            owner=request.user,
            expiry_date__isnull=False
        ).order_by("expiry_date")

        actions = []
        today = date.today()

        for document in documents:

            status = document.get_status()

            if status in ["EXPIRING", "ACTION_REQUIRED"]:

                actions.append({
                    "title": document.title,
                    "family_member": document.family_member.full_name,
                    "document_type": document.document_type,
                    "action": f"Renew {document.get_document_type_display()}",
                    "days_left": (document.expiry_date - today).days,
                })

        serializer = MonthlyActionSerializer(actions, many=True)
        return Response(serializer.data)
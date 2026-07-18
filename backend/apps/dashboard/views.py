from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.documents.models import Document
from apps.users.models import FamilyMember

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
    
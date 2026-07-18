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
from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = "__all__"
        read_only_fields = ["id", "owner", "created_at"]

    def get_status(self, obj):
        return obj.get_status()
    
    def validate(self, data):
        expiry_required = [
          "PASSPORT",
          "DL",
          "INSURANCE",
        
        ]

        if (
            data.get("document_type") in expiry_required
            and not data.get("expiry_date")
        ):
            raise serializers.ValidationError(
                {
                   "expiry_date": "This document type requires an expiry date."
                }
           )

        return data
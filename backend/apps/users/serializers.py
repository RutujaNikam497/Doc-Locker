from rest_framework import serializers
from .models import FamilyMember


class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = ["id", "full_name", "relation", "date_of_birth", "mobile", "created_at"]
        read_only_fields = ["id", "created_at"]
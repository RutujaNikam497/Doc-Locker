from rest_framework import serializers


class UpcomingDocumentSerializer(serializers.Serializer):
    title = serializers.CharField()
    family_member = serializers.CharField()
    document_type = serializers.CharField()
    expiry_date = serializers.DateField()
    status = serializers.CharField()
    days_left = serializers.IntegerField()

class MonthlyActionSerializer(serializers.Serializer):
    title = serializers.CharField()
    family_member = serializers.CharField()
    document_type = serializers.CharField()
    action = serializers.CharField()
    days_left = serializers.IntegerField()
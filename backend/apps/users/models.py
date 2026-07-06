from django.conf import settings
from django.db import models


class FamilyMember(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="family_members"
    )
    full_name = models.CharField(max_length=120)
    relation = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.relation})"
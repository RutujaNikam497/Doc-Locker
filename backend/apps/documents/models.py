from django.conf import settings
from django.db import models
from apps.users.models import FamilyMember
from datetime import date, timedelta

class Document(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    family_member = models.ForeignKey(
        FamilyMember,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    title = models.CharField(max_length=150)

    DOCUMENT_TYPES = [
    ("AADHAAR", "Aadhaar Card"),
    ("PAN", "PAN Card"),
    ("PASSPORT", "Passport"),
    ("DL", "Driving Licence"),
    ("INSURANCE", "Insurance"),
    ("OTHER", "Other"),
    ]

    document_type = models.CharField(
    max_length=20,
    choices=DOCUMENT_TYPES
    )

    STATUS_CHOICES = [
    ("VALID", "Valid"),
    ("EXPIRING", "Expiring Soon"),
    ("ACTION_REQUIRED", "Action Required"),
    ]

    
    file = models.FileField(upload_to="documents/")

    issue_date = models.DateField()

    expiry_date = models.DateField(null=True, blank=True)

    #status = models.CharField(
    #    max_length=20,
    #    choices=STATUS_CHOICES,
    #    default="VALID"
    #)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_status(self):
      if self.expiry_date is None:
        return "NO_EXPIRY"

      today = date.today()

      if self.expiry_date < today:
        return "ACTION_REQUIRED"

      elif self.expiry_date <= today + timedelta(days=30):
        return "EXPIRING"

      return "VALID"

    def __str__(self):
        return self.title
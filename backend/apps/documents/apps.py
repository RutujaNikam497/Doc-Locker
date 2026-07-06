from django.apps import AppConfig

class DocumentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.documents"
    #above name is path to the app, it is used by django to identify the app in the project
    
from django.apps import AppConfig


class DirectMessagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "direct_messages"
    verbose_name = (
        "Direct Messages"  # To change the display name from Direct_Message to Direct Message
    )

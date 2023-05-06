from django.apps import AppConfig


class smb_usersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smb_users'

    def ready(self):
        import smb_users.signals

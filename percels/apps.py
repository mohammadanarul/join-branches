from django.apps import AppConfig


class PercelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'percels'

    def ready(self):
        import percels.signals

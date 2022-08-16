from django.apps import AppConfig


class PetstoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petstore'

    def ready(self) -> None:
        import petstore.signals
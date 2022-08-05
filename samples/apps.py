from django.apps import AppConfig


class SamplesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'samples'

    def ready(self):
        # everytime server restarts
        import samples.signals


from django.apps import AppConfig
class SecAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sec_app'

    def ready(self):
        import sec_app.signals

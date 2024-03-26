from django.apps import AppConfig

class NewsScrapperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_api'

    def ready(self) -> None:
        return super().ready()
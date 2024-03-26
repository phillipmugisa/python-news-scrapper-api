from django.contrib import admin
from . import models

admin.site.register(models.NewsArticle)
admin.site.register(models.NewsSource)

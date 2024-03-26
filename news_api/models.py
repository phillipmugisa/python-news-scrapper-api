from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class NewsSource(models.Model):
    name = models.CharField(
        _("News Source"),
        max_length=500,
        blank=False,
        null=False
    )
    base_url = models.URLField(
        _("Base Url"),
        blank=True,
        null=True
    )
    added_on = models.DateTimeField(
        _("Upload On"),
        default=timezone.now,
    )

    def __str__(self) -> str:
        return f'{self.name}'

class NewsArticle(models.Model):
    class Meta:
        ordering = ("-added_on",)

    title = models.TextField(
        _("News Headline"),
        blank=False,
        null=False
    )

    category = models.CharField(
        _("Category"),
        max_length=500,
        blank=False,
        null=False
    )

    description = models.TextField(
        _("News Description"),
        blank=True,
        null=True
    )

    source = models.ForeignKey(to=NewsSource, related_name="Source", on_delete=models.CASCADE)

    url = models.CharField(
        _("News Url"),
        blank=False,
        null=False,
        max_length=500
    )
    img_url = models.CharField(
        _("Image Url"),
        blank=False,
        null=False,
        max_length=2000
    )
    posted_on = models.DateTimeField(
        _("Posted On"),
        blank=True,
        null=True
    )
    added_on = models.DateTimeField(
        _("Upload On"),
        default=timezone.now,
    )

    def __str__(self) -> str:
        return f'{self.source} - {self.title}'
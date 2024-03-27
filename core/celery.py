from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab


# set django setting module environment variable for celery program

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")

# auto discover tasks in other apps
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "scrap_news_daily" : {
        "task": "news_api.tasks.scrap_news",
        "schedule": crontab(minute=0, hour="0,12")
    }
}

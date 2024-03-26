from celery import shared_task
from news_api import models, serializers

@shared_task
def scrap_news():
    from news_scrapper.run_scrapper import run_scrapper

    save_to_db(run_scrapper())


def save_to_db(scrapped_data : list) -> None:

    for group in scrapped_data:
        
        if not models.NewsSource.objects.filter(name=group["source"]).exists():
                models.NewsSource.objects.create(name=group["source"], base_url=group["url"])

        for data in group["results"]:
            source_id = models.NewsSource.objects.get(name=group["source"]).pk
            
            articles = list(map(lambda obj: {
                **obj,
                'category': data.get('category'),
                'source_id' : source_id
            }, data.get('articles')))

            serializer = serializers.NewsSerializer(data=articles, many=True)

            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
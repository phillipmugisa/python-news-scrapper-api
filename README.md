# python-news-scrapper-api

This is a news scrapper python app that exposes an api.

## Requirements
- Django
- beautifulsoup4
- celery

## Available Sources
- Google News
- New York Times
- Yahoo News

## Available Categories
- Technology
- Entertainment
- Fashion
- Sport

## Usage

### Base URL
http://127.0.0.1:8000/news

### Filter by Category
http://127.0.0.1:8000/news/?category=entertainment

### Filter by Source
http://127.0.0.1:8000/news/?source=Google%20News

### Filter by Category and Source
http://127.0.0.1:8000/news/?category=entertainment&source=Google%20News

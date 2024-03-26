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
http://newsscrapper.mugisa.tech/news

### Filter by Category
http://newsscrapper.mugisa.tech/news/?category=entertainment

### Filter by Source
http://newsscrapper.mugisa.tech/news/?source=Google%20News

### Filter by Category and Source
http://newsscrapper.mugisa.tech/news/?category=entertainment&source=Google%20News

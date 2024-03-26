# Python News Scrapper

**Author:** Phillip Mugisa  
**Date:** 6/08/2022  
**Updated:** 26/03/24  

---

This program scrapes news from top news platforms, allowing users to view news based on location and category.

## Requirements
- beautifulsoup
- requests

## Sources
- Google News
- New York Times
- Yahoo News

## Categories
- Technology
- Entertainment
- Fashion
- Sports
- Finance

## Locations
- Global
- USA
- Europe
- Africa

## Data Structure
```json
{
    "category": "______",
    "count": "______",
    "articles": [
        {
            "title" : "______",
            "description" : "______",
            "img_url" : "______"
        }
    ]
}
